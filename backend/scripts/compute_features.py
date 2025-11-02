#!/usr/bin/env python3
# Orchestrate feature computations:
# - Update access_score from travel_time_snapshot (transform lower minutes -> higher score)
# - Update amenity_index from amenities_snapshot
# - Update infra_uplift using nearest metro distance buckets
