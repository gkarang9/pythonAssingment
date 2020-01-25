'''import pickle 
phonebook={'aaa':'4353'}
out_file=open('phonebook.dat','wb')
pickle.dump(phonebook,out_file)
out_file.close()'''

'''import pickle
in_file=open('phonebook.dat','rb')
print(pickle.load(in_file))'''

import pickle
in_file=open('phonebook.dat','rb')
pb=pickle.load(in_file)
in_file.close()
print(pb)