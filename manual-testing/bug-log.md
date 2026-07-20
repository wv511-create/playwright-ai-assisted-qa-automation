## BUG-01: Booking succeeds with invalid registration credentials

**Severity:** High
**Steps to reproduce:**
1. Open the app and select the Farmer role
2. Enter an invalid phone number (e.g. wrong length, non-numeric, or clearly
   fake) in the registration form, along with a name and village
3. Proceed to browse and book any available machine
4. Complete the booking flow through to confirmation

**Expected result:** Registration should validate the phone number format
before allowing the user to proceed, since the phone number is later used as
the point of contact between farmer and owner.

**Actual result:** The invalid phone number is accepted at registration with
no validation, and the user is able to complete an entire booking using this
unverified contact information.

**Notes:** This is more than a data-quality issue — it means a booking can be
confirmed with contact details the owner can't actually use to reach the
renter, which breaks the core purpose of the booking (owner is meant to be
notified and able to contact the farmer).

---

## BUG-03: Machine category filter buttons non-functional

**Severity:** High
**Steps to reproduce:**
1. Register and reach the equipment browsing screen
2. Confirm all 6 machines are visible under the "All" filter
3. Click a specific category filter, e.g. "Tractor" or "Harvester"

**Expected result:** The listing should update to show only machines matching
the selected category.

**Actual result:** Clicking a category filter button has no effect — the
button does not appear to register the click, and the full unfiltered list
remains displayed regardless of which category is selected.

**Notes:** Confirmed this is not a "returns zero results" issue — the buttons
appear entirely unresponsive to interaction.

---

## BUG-04: Search does not return or update results

**Severity:** High
**Steps to reproduce:**
1. Reach the equipment browsing screen
2. Type a machine name or type into the search field (e.g. "tractor")
3. Click the search button

**Expected result:** The listing should filter to show only machines matching
the search term.

**Actual result:** Nothing happens after clicking search — the listing does
not update, and no error, loading state, or empty-results message appears
either.

**Notes:** Worth checking browser console for a JS error on this action
specifically (open DevTools → Console before triggering search) — the total
lack of visible response suggests the click handler may not be wired up at
all, rather than a filtering-logic bug.

---

## BUG-05: Cancel Booking button does not respond to clicks

**Severity:** High
**Steps to reproduce:**
1. Complete a booking through to confirmation, landing on the booking status
   screen (Pending/Accepted/Declined tabs)
2. Locate the booked machine's card and click "Cancel"

**Expected result:** The booking should be cancelled, with the machine either
removed from the list or its status updated to reflect cancellation.

**Actual result:** Clicking Cancel produces no visible effect — the booking
remains listed as Pending with no change in state, no confirmation prompt,
and no error.

**Notes:** No workaround currently exists for a farmer to cancel a mistaken or
unwanted booking, which makes this High rather than Medium — it's a dead end
in the flow, not just a rough edge.

---

## BUG-08: Accepted / Declined tabs do not switch the displayed view

**Severity:** High
**Steps to reproduce:**
1. Complete a booking so it appears under the Pending tab
2. Click the "Accepted" tab
3. Click the "Declined" tab

**Expected result:** Each tab should switch the visible list to show only
bookings in that respective status (even if empty, since this booking is
still Pending, Accepted/Declined should at least render an empty state for
it).

**Actual result:** Clicking either tab has no visible effect — the view stays
on whatever was last displayed, with no indication the tab selection changed
at all.

**Notes:** Since there's currently no way to test with a booking that's
actually in an Accepted or Declined state (no flow exists yet to change a
booking's status), this may partly be an untestable/unimplemented feature
rather than a broken one — worth a follow-up check on whether backend/status
transition logic exists at all before treating this purely as a UI bug

