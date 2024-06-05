class polisi :
    def __init__(self ,jenis):
        self.jenis = jenis   
 
    def jobdesk(self):
        pass

class Polisi_lalin(polisi):
    def jobdesk(self):
        return ('mengatur lalu lintas')

class Polisi_patwal(polisi):
    def jobdesk(self):
        return ('untuk mengawal')

class Polisi_tidur(polisi):
    def jobdesk(self):
        return ('untuk dilindas')
    
    
polisi_lalin = Polisi_lalin('Wahyu sebagai polisi lalin' )
polisi_tidur = Polisi_tidur('Pandu sebagai polisi tidur' )
polisi_patwal = Polisi_patwal('Aziz sebagai polisi patwal' )

print(f'{polisi_lalin.jenis} bertugas {polisi_lalin.jobdesk()}')
print(f'{polisi_patwal.jenis} bertugas {polisi_patwal.jobdesk()}')
print(f'{polisi_tidur.jenis} bertugas {polisi_tidur.jobdesk()}')

