import csv
import random

from faker import Faker


class TestCSV(object):

    def __init__(self, fake=Faker()):
        self.fake = fake

    def randspace(self, max_mul=10):
        """Return whitespace of random length: 1 to max_mul."""
        return ' ' * random.randint(1, max_mul)

    def gen_bio(self):
        """Return randomly tab/newline/space-delimited lorem text."""
        padding = ['\t', '\n', self.randspace()]
        sentences = self.fake.sentences(nb=3)
        # arbitrarily pad the sentences
        for _ in xrange(random.randint(1, 3)):
            rand_idx = random.randint(0, len(sentences)-1)
            rand_sentence = sentences[rand_idx]
            sentences[rand_idx] = rand_sentence + random.choice(padding)
        return ' '.join(sentences)

    def gen_sex(self):
        """Return random choice of 'M' or 'F'."""
        return random.choice(['M', 'F'])

    def gen_state_abbr(self):
        """Return random choice of US state abbreviation."""
        state_abbrs = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL',
            'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
            'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM',
            'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN',
            'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
        return random.choice(state_abbrs)

    def gen_startdate(self):
        """Return random choice of date, invalid date, or lorem text."""
        valid_date_patterns = ['%B %-d, %Y', '%m/%d/%Y', '%Y-%m-%d']
        invalid_date_patterns = ['%m/%y', '%B %Y']
        return random.choice([
            self.fake.date(pattern=random.choice(valid_date_patterns)),
            self.fake.date(pattern=random.choice(invalid_date_patterns)),
            self.fake.text(max_nb_chars=20)])

    def create_row(self):
        """Return row of fake data."""
        return [self.fake.name(), self.gen_sex(), self.fake.date(),
            self.fake.street_address(), self.fake.city(),
            self.gen_state_abbr(), self.fake.postalcode(), self.fake.email(),
            self.gen_bio(), self.fake.job(), self.gen_startdate()]

    def write_csv(self, filename, header):
        """Write CSV file to working dir."""
        with open(filename, 'wb') as fh:
            writer = csv.writer(fh)
            writer.writerow(header)
            for _ in range(500):
                row = self.create_row()
                writer.writerow(row)

if __name__ == '__main__':
    test_csv = TestCSV()
    test_csv.write_csv('test.csv', ['name', 'gender', 'birthdate', 'address',
        'city', 'state', 'zipcode', 'email', 'bio', 'job', 'start_date'])
