There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer array position and speed, both of length n,
where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = 0
        position_speed = sorted(zip(position, speed))
        times_to_reach_target = []

        for pos, spd in position_speed:
            times_to_reach_target.append((target-pos)/spd)

        current_time = 0

        for time in reversed(times_to_reach_target):
            if time > current_time:
                car_fleet += 1
                current_time = time
        return car_fleet