class Path(object):
    @staticmethod
    def db_dir(database):
        if database == 'myhands':  # ucf101改为myhands
            # folder that contains class labels
            # 这里没改，以ucf101作为database的名称，后续需要改动
            # root_dir = 'E:\\eclipse-workspace\\PyTorch\\pytorch-video-recognition-master\\data\\UCF-101'
            # 改为自己的路径
            root_dir = "D:\\AIProj\\3DCNNhandsDec\\data\\handsdection"

            # Save preprocess data into output_dir
            # output_dir = 'E:\\eclipse-workspace\\PyTorch\\pytorch-video-recognition-master\\data_process\\ucf101'
            output_dir = 'D:\\AIProj\\3DCNNhandsDec\\datatest\\headsdectionProcess'

            return root_dir, output_dir
        elif database == 'hmdb51':
            # folder that contains class labels
            root_dir = '/Path/to/hmdb-51'

            output_dir = '/path/to/VAR/hmdb51'

            return root_dir, output_dir
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def model_dir():
        # return './model/c3d-pretrained.pth'
        # 改动
        return './model/c3d-pretrained-changed.pth'
