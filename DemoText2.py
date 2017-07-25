
data = [[1,1,-1],
		[2,0,0],
		[3,1,1],
		[4,0,-1]]
ds = Dataset(data)
print(type(Dataset(data)))#class 'mvpa2.datasets.base.Dataset
print(ds.shape)
print(len(ds))
print(ds.nfeatures)#特征数目
ds.samples
print(type(ds.samples))#<class 'numpy.ndarray'>
one_d = [0,1,2,3]
one_dz = Dataset(one_d)
one_dz.shape#<class 'tuple'>
print(type(one_dz.shape),one_dz.shape)
m_dz = Dataset(np.random.random((3,4,2,3)))
m_dz.shape
#print(tyep(m_dz))
m_dz.nfeatures
print(m_dz.shape,m_dz.nfeatures)
#MVPA attributes samples
ds.sa['some_attr'] = [0.,1,1,3]
ds.sa.keys()
print(ds.sa.keys)
tyt = (ds.sa['some_attr']).value
print(type(ds.sa))#class 'mvpa2.base.collections.SampleAttributesCollection
print(len(ds.sa['some_attr'].unique))

ds1 = ds[:2].samples
#print(ds1)
mask = np.array([True,False,True,False])#使用布尔值来选择dataset被切片出来的样本
print("value")
print(ds[mask].samples)
print("000")
print(ds[[0,2]].samples)