#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

// Minutes since 00:00 of Monday
using job_time_t = int;

// Minutes
using job_duration_t = int;

using detail_id = int;

enum Machines { A, B, Count };
enum Events { Delivery, Ended };

struct answer_t {
  int delayed_details_count;
  job_time_t end_time;
};

struct detail_t {
  job_time_t delivery_time;
  job_duration_t processing_duration[Machines::Count];
  int first_machine;
};

struct event_t {
  int type;
  detail_id detail;
};

istream& operator>>(istream& in, detail_t& out) {
  in >> out.delivery_time;
  for (int machine : {A, B})
    in >> out.processing_duration[machine];

  string first_machine_word;
  in >> first_machine_word;

  for (auto& [word, key] : {pair<string, int>{"A", A}, {"B", B}}) {
    if (first_machine_word == word)
      out.first_machine = key;
  }

  return in;
}

vector<detail_t> parse_input() {
  ifstream file("rc/26.txt");

  int details_count;
  file >> details_count;

  vector<detail_t> details(details_count);

  for (auto& detail : details)
    file >> detail;

  return details;
}

answer_t solve(const vector<detail_t>& details) {
  answer_t answer{.delayed_details_count = 0, .end_time = -1};

  unordered_map<job_time_t, vector<event_t>> events;

  for (detail_id id = 0; id < details.size(); ++id) {
    event_t delivery_event{.type = Delivery, .detail = id};
    int delivery_time = details[id].delivery_time;
    events[delivery_time].push_back(delivery_event);
  }

  detail_id current_detail[Machines::Count];
  queue<detail_id> q[Machines::Count];
  set<detail_id> waiters;

  for (int machine : {A, B})
    current_detail[machine] = -1;

  for (job_time_t t = 0; t < 100000; ++t) {
    sort(events[t].begin(), events[t].end(),
         [](const event_t& lhs, const event_t& rhs) {
           return (lhs.type == Ended && rhs.type == Delivery) ||
                  (lhs.type == rhs.type && lhs.detail < rhs.detail);
         });

    for (const auto& event : events[t]) {
      detail_id id = event.detail;

      switch (event.type) {
        case Ended: {
          for (int machine : {A, B}) {
            if (current_detail[machine] == id) {
              if (machine == A)
                answer.end_time = t;

              current_detail[machine] = -1;

              if (details[id].first_machine == machine)
                q[(machine + 1) % Machines::Count].push(id);

              break;
            }
          }
          break;
        }

        case Delivery: {
          int machine = details[id].first_machine;
          q[machine].push(id);
          break;
        }

        default:
          break;
      }
    }

    for (int machine : {A, B}) {
      if (current_detail[machine] != -1)
        continue;

      if (q[machine].empty())
        continue;

      detail_id id = q[machine].front();
      q[machine].pop();

      current_detail[machine] = id;

      event_t ended_event{.type = Ended, .detail = id};
      auto duration = details[id].processing_duration[machine];
      events[t + duration].push_back(ended_event);
    }

    auto qa = q[A];
    while (!qa.empty()) {
      waiters.insert(qa.front());
      qa.pop();
    }
  }

  answer.delayed_details_count = waiters.size();

  return answer;
}

int main() {
  auto details = parse_input();
  auto answer = solve(details);

  cout << answer.delayed_details_count << ' ' << answer.end_time << endl;
}

// Answer: 747 10038