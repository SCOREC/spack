# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack import *

RELEASES = [
    {
        'version': '16.0-220312',
        'components': {
            'msparalleladapt': ['cc6d6ecba8183f3444e55977af879b297977ff94dd7f6197028110f7e24ea60b', 'paralleladapt'],
            'msadapt': ['ec4a985f9b29914411d299fecfb1a994224070480be5de5f701d9968ba9da9e5', 'base'],
            'opencascade': ['008e7232ee3531b70143129e5a664f7db0e232bad9d11d693d725d39986a8aa4', 'opencascade'],
            'gmvoxel': ['4a74c54c31e9eb93f9a0c09ef3ac88f365efb19666240374aa6d1142db993a2c', 'voxel'],
            'msadv': ['d33b591147152383130cc2190f1bd7726cb9ea3590468691db3be5815802d888', 'adv'],
            'pskrnl': ['e154c22c01ecab2e041cf5d87fcb23eab074449dae7f677f17e7863b6da70fdc', 'parasolid'],
            'gmcore': ['d9ed89d07d83f2c23eca6a27fd9000fd4c8eeefa70ac860aa28a40000a6ec93e', 'base'],
            'psint': ['5c236e429f28a36a36cb09ec3f4778dc7b6e72447014b684792eea733bb21fd5', 'parasolid'],
            'msparallelmesh': ['a791f4464da54faafdc63dbcaf3d326ffc49c9ea8d53e36cc57c15607cf72db9', 'parallelmesh'],
            'mscore': ['48e367e476a03a9fa5389830a6c60824b5d620d04d87392e423a33a331ba3595', 'base'],
            'fdcore': ['022de14021434d90daee8ea1200c024d98a7eb01bb9cb5a06a3b2f7ffee9c0a1', 'base'],
            'gmadv': ['6232ec08ef5cff4269d066b035490f33c199fb545355836ef1536b1a00179b2c', 'advmodel'],
            'gmabstract': ['08a6c7423ed59361c5330dbe00b8914d1d55160de73002e7e552c45c8316f37a', 'abstract'],
            'discrete': ['f5ae00688cf202e75686955185d95952e7b581b414dd52bfef0d917e5959ab22', 'discrete'],
            'aciskrnl': ['c2c7b0c495d47a5662765f1b0c6f52863032e63384d85241e6313c4b773e9ed2', 'acis'],
        },
        'docs': {
            'GeomSimParasolid': ['3420fcc1ac67cff8f46b79553cfe478f34676b9b0cd1fa913255b48cbdfd6ad4', 'parasolid'],
            'GeomSimAcis': ['77b31bfb368f1e7981b3a81087e4e287c560e0a0cd08920b36dc81fea25bcdfa', 'acis'],
            'MeshSimAdvanced': ['abeeb0cb10cf3074295a880412e0568b653f2784b1de19f0f8ede5eec536a8bd', 'adv'],
            'GeomSim': ['b1e762111eb8025b966b0aca4bef3768325d9f1c1e3c72a1246b59539e444eb2', 'base'],
            'GeomSimVoxel': ['bc43f931670657a2cae79f9a2a02048b511fa6e405f15e583631e9f6888e7000', 'voxel'],
            'ParallelMeshSimAdapt': ['dd3a0fd6b889dadb45f9a894f684353fffa25bf15be60ae8e09d0c035045e192', 'paralleladapt'],
            'GeomSimAdvanced': ['3e971ae069baf94b38794318f97f16dc25cf50f6a81413903fbe17407cbd73b3', 'advmodel'],
            'GeomSimGranite': ['e438c19bb94a182068bf327988bd1ff9c1e391876cd9b7c74760b98cbfd08763', 'granite'],
            'FieldSim': ['5ede572cbb7539921482390e5890daa92399a5f1ee68a98d3241a7d062667d9d', 'base'],
            'MeshSimAdapt': ['c4be287da651c68e246034b28e141143d83fc3986fd680174a0d6de7b1cc35ab', 'base'],
            'GeomSimOpenCascade': ['34a8d628d07ab66159d6151276e93fdabfcc92a370f5927b66a71d3a8545652c', 'opencascade'],
            'GeomSimDiscrete': ['d2b11367334401ec57390a658715e91bbf3e3a0e8521fab1ad5d3f7c215b2921', 'discrete'],
            'GeomSimAbstract': ['601b0179b65a385a39d241a9a4e3074e4f834c817e836bea07516015c769e666', 'abstract'],
            'GeomSimDiscreteModeling': ['619b8254d8e3bcc94e84551e997b577dd9325131d084c3b3693ab665b7e4213b', 'discrete'],
            'ParallelMeshSim': ['5b74b9b5f9290111366e341c12d4777635e375523d42cb0a2b24aa1bfa8ab8c4', 'parallelmesh'],
            'MeshSim': ['2f1944e1853a550cc474201790555212e4b7a21d3675715de416718a789ccae2', 'base'],
        }
    },
    {
        'version': '2023.1-230907dev',
        'components': {
           'fdcore': ['cdb3e937c064ebfb7f8c45b5de7cff7e4ca4a727d3a33e979f62687dab2b8bf8', 'base'],
           'mscore': ['38b3e9ea02872ac0a760df5c0cb9999f6afef43905a9a78c9a63ce79e3b2c176', 'base'],
           'gmadv': ['ab942e2e9f118811dddb8bc812b662b752176a6aa61f16847d713e8e197469f8', 'advmodel'],
           'msparallelmesh': ['2bb9d824d1cec9a9b983713d0f4cb980e44a99d8f25f74ae87d3162c8cabd9bd', 'parallelmesh'],
           'aciskrnl': ['c8512becbc1b42ef2a787f0144b5bace01753c9538f4a39efa6613c3998fae56', 'acis'],
           'mscrack': ['d51f979420026f987795c538c5365ca6243a69b1dfe481037f874e7abfc53ffe', 'crack'],
           'discrete': ['0fc27c2705ff5d90f3daa8bca25288f83326a33cc39f4101465bb7df346b3617', 'discrete'],
           'msadv': ['4eb40f73181219336b57e8c6b07eb64f43f8e99b74ff19b447c0d72e9e821e8e', 'adv'],
           'psint': ['d660e3a79f0912de98fb94a585ca106a2027d1f14b2eb586292d5b5eef24261d', 'parasolid'],
           'gmabstract': ['0204acf10f39feaadcd34e99a4603d5e92a37b0ec2357c0d0134ec8397fe184a', 'abstract'],
           'gmcore': ['3fd94c35d6336ccd22f6925c994907608880eb0ad11db188a87f12dd40f373c8', 'base'],
           'pskrnl': ['c36423e668788a77669578cf3a0919ace279c7fa2fcf640964dc8e5b002bf109', 'parasolid'],
           'gmvoxel': ['26535d3482ff975a5270ecff093c4bc3d9ebf3eaf1bce2d0bfb0f6c66a2431c8', 'voxel'],
           'msparalleladapt': ['80457230df9907f001deedc3aa50dc28c4d19e775fe466fa7c54648a47c4e65a', 'paralleladapt'],
           'msadapt': ['50fcf225404f7f42c703db2d44687075dd4ce410449ed0c39864224c2b3ecb1d', 'base'],
        },
        'docs': {
           'GeomSimVoxel': ['84aff0bd3d30e29992891ddf3fddb566dbc485ad707eb35e6474b8ad9ebe1143', 'voxel'],
           'GeomSimAbstract': ['9f9cef2df87eb551a2062cc501e78b8a53d110e739b5457622cd0f1797f439fa', 'abstract'],
           'GeomSimDiscrete': ['8e8a6b4a1be69fd70c9be08d7789628a1986928b3f533d477f22dc1aa88d5579', 'discrete'],
           'GeomSimDiscreteModeling': ['483ad15c37647688e8c9b7e84b6c98f66f43bad37adcab54d60b78a348679a32', 'discrete'],
           'GeomSimAcis': ['c375a01c086e3a01b27585dff6dd94acf2dff27e54e168c69515e2b7364ae2cf', 'acis'],
           'GeomSim': ['4a09ca7a2eb54092cea58f56e8ae5a56e2bc5d2f53b8aebca9ac24d4d0c996c7', 'base'],
           'ParallelMeshSim': ['f0b4136346668bba3998f5dc21468160897e7abe9bbb0fec43a05444968933ad', 'parallelmesh'],
           'FieldSim': ['28a3788c63b4750b50309ba7876997e5623bb00fb3e22fdf8f66126a29f6c618', 'base'],
           'GeomSimParasolid': ['f769e7d91a5d8023c61255c97ffb16823f5161a537bb93d236681d7a80a2c9fd', 'parasolid'],
           'GeomSimAdvanced': ['67e7b68d794d8ff564353fdddd54dc08fbdb01cef99ee9779763cdcdb4d6e656', 'advmodel'],
           'ParallelMeshSimAdapt': ['2948739c44b363f7360f77133f637b1198314f9da591ebd4cc11d81dc1889a00', 'paralleladapt'],
           'MeshSimAdapt': ['245b6fd49c2cc3f51c474f2429cb0f8ab0387d610d1f3c0434f4069d181bd024', 'base'],
           'MeshSimCrack': ['545c3e151a3b246ce180833c07149062ca4002f16ecd94ffbd64fd1a325b020b', 'crack'],
           'MeshSimAdvanced': ['dd8f9d684e0bd1acf6c7fed7d40b25084b65689b27881e2c4104c69aea566cea', 'adv'],
           'MeshSim': ['0e638eafc6eb3d695d6b29dba1f15fa09b6d48b4fe5f9ea806c884d6824b11eb', 'base'],
        }
    },
    {
    'version': '2023.1-230428dev',
    'components': {
       'msparalleladapt': ['16c886fe9556b90fea99e2b76b9b679cd2f044ac73764939881361009df7776d', 'paralleladapt'],
       'pskrnl': ['e852750446c2ca98d0c8b47d83d8dcd087a2c10b0a6683a878d9eba4c167b59a', 'parasolid'],
       'msadv': ['ccd3e2f69cf1ca637b0fae0ae1dc8d16e73569ad51cf65e667d262a8bcef0e00', 'adv'],
       'gmcore': ['b2dfebf01755437ea20942d91177ced1c5445d8f868d8b8023bfb49682ded11b', 'base'],
       'psint': ['b91d28606182bf1efe286708da43d57d00dd482f06ee8cb0ade3f6e53c73f164', 'parasolid'],
       'mscrack': ['5a70fd3ea9b4dfca91d142c10820d0f8935fa85bfaab5ca14070f1dab470ea13', 'crack'],
       'aciskrnl': ['2f0c328ffde7bea1a735ae2609f9395e70630d8d4eb51bc34934c0d6c3d58753', 'acis'],
       'gmadv': ['007c5422350c48b3b072d68d44dcd4832245565119e3041ffb9ac3d67b4dfd22', 'advmodel'],
       'discrete': ['beec74b4b01c735736a39ad1a7f58b380717eb07bc6aa89287a5ad2679053682', 'discrete'],
       'msparallelmesh': ['5d5db7e62893f2dce8ce85b3601784799654b5cea2f87a05e30563d5f7c55148', 'parallelmesh'],
       'gmvoxel': ['9348c3445ce6cdff39fa801818fe9a320615757981de75dee415aa1197cb231f', 'voxel'],
       'fdcore': ['d3291a9da8e3ee9fb9ac373e4ceca701881d2ada04734718b42fc2074d1b77fb', 'base'],
       'msadapt': ['b5d33b4896a17ed13c9e4961e9f41c55683935eec266aa9545a71574706c2aa3', 'base'],
       'gmabstract': ['3b85b3949f84eab105cb8775f582431f341d0f956c501017213bc2faeb897fd9', 'abstract'],
       'mscore': ['708dbafb07e0bdccc2e820f18e9019eceb49bff39ae729c11bf930f003acadd2', 'base'],
       },
    'docs': {
       'GeomSimAbstract': ['af057e1f2f3e071fe9eacee5fbd48309682bfd04c7b0c879bd8612cbc34e791b', 'abstract'],
       'GeomSimDiscrete': ['52d29bb2820f9643b8c233b0f6c3509acb9532bbab18ce9bcc437fb1a8e987fe', 'discrete'],
       'GeomSim': ['539fea7130c62aaa313cc8414628bb68f66277d7d20c3320d4ed6c3e46bcd398', 'base'],
       'GeomSimParasolid': ['c54888b3bad1604dff6c26091554239a47e268d185169d630c55485a3e62ffde', 'parasolid'],
       'ParallelMeshSim': ['5541a0b50b66adcbb55f2043b54d3d6a346b51876e15dc6cc317589e2b3de505', 'parallelmesh'],
       'ParallelMeshSimAdapt': ['ae4f010223cceb9ff4771e3c333ec81d5a471a1b71dccfbcdedcc526970f429d', 'paralleladapt'],
       'GeomSimAcis': ['567728de91e5cd310e5d6ae4ec3e8fe354a02952ca6f96072ef2f5acd17c435c', 'acis'],
       'GeomSimVoxel': ['8ed2f0ccde70fb4f9e35a74de4d9584ec778eca16ab00f17acf9603c4831572f', 'voxel'],
       'FieldSim': ['420c06fc0867fc7dc5d6c2bdf9eb6abd5116a9c5cb3427286ebd17def1b7ec6d', 'base'],
       'MeshSimAdvanced': ['3c9ff434e6c101dfe712c0943aa6beab8d47fdc6735ab5df4a154453f949e5b7', 'adv'],
       'GeomSimAdvanced': ['ab829df31bb690073a761abc69be3e24172b811b0ba946beef3aa4491e1af2ae', 'advmodel'],
       'GeomSimDiscreteModeling': ['3f620a3df57060d4c063a6f236e709884a3c67dcac763aa797cdbb81b8d14bda', 'discrete'],
       'MeshSimCrack': ['4e1cb0f4d073a7a59998c3099ccb6346ca66746cca3080b734b593c0745266a1', 'crack'],
       'MeshSimAdapt': ['ed3350b849fd7c1a220815b95a4af3c6c822f3efc53e847217da03b9de15256b', 'base'],
       'MeshSim': ['40eee3108c01f299d16c8de8583cbffbed54af2ecf135a8b6fec046b796b4502', 'base'],
       }
    },
    {
    'version': '2023.0-230317dev',
    'components': {
       'gmadv': ['d966d5e99fc395647670a4b03725b4049bb59f6bf8a87e908125270d0bbd6cb7', 'advmodel'],
       'gmvoxel': ['c51b71ae113dc6bf1aa7af6b8cd55372a96f365eaec39f7e2dbf2551682f39a6', 'voxel'],
       'msadapt': ['7340427d63f029862373290d622bba7227d24b3bbee7872458d0f9d20e34ccd5', 'base'],
       'pskrnl': ['33d09f267811fc98821418ad47c37fef2ea1b60cdfa2f8b20dddd0a27daaa726', 'parasolid'],
       'gmcore': ['4cfe35f3a37372735a433504f3f5731799b8b83413a3f3fb1dbcb8d288123322', 'base'],
       'fdcore': ['d31a2a6728380d30864a56d31f709efcd0f2874c3c651e8d7740b79820589c00', 'base'],
       'aciskrnl': ['562f69d82199bfc3db7575ec502e05115d6a6b8684a236d932f5d59fe28e03b0', 'acis'],
       'discrete': ['879e74bc7f7fb9832e64012ea9924f08c012f1e8b06a3e9c0b660c03e2969c61', 'discrete'],
       'msadv': ['69d052e4557d2729b85873a2fdf4cf235388399798a61b3dff32337c86a5e916', 'adv'],
       'psint': ['e26a3b93a0f32e3a3734954046a40c85bbf95b579774b0e723ad17a3d52b1595', 'parasolid'],
       'msparallelmesh': ['c5eb773ae41254ba39939f7215c63b703ada8fd5fdb87280b88a7965f90c39bf', 'parallelmesh'],
       'mscore': ['85a4750995b37acfe05364d8a17537d39a70e8ae7cfa4aaf8b768f0fc12d7a39', 'base'],
       'gmabstract': ['690c3e9cea7c979efa160ba928822fa8c4d36626449855a8ff393f2e7915ef53', 'abstract'],
       'msparalleladapt': ['dfefbd86aaaadf8a00d841b3268550e93b14ef033dcb1863e0a27b536580f6cf', 'paralleladapt'],
       },
    'docs': {
       'GeomSimDiscreteModeling': ['f9f80b614576af0b9f590fae4611ef4bb08798ccfb408a274ca292fcd280b514', 'discrete'],
       'GeomSimVoxel': ['5f6afdaf1a4f07eda0eee6b122699f5acfc92419aeee17a11b10a58e2d52f318', 'voxel'],
       'GeomSimAdvanced': ['42a341e5d4b8cf96685dffa2a6b50455c5d522e2f5556e9b1c4d5fd909d46bfc', 'advmodel'],
       'ParallelMeshSimAdapt': ['ffb8ea0dcf5ad0c04de6fa0a392c5b9f670c1d6d28408f0dd579af9bbbdc5a4e', 'paralleladapt'],
       'MeshSimAdvanced': ['1a51b56f2d2735ad6bb9c3a03ec2a4c3f8352a8b6bd468ab86b0dc1a4151869d', 'adv'],
       'GeomSimParasolid': ['2948d33bbe4fccff10360627ebd05ef4d488e4a0dbf39acc635ee6c0b3297dc3', 'parasolid'],
       'GeomSim': ['4eeb717ab86c1654bf084bb8451ae60a3aaceab78176239c221d23ce37709ba1', 'base'],
       'MeshSimAdapt': ['3085154835abf6f95f3d800e2def96b1aa9351244db350579bb3be66141dc759', 'base'],
       'ParallelMeshSim': ['1c3c586a2046d7603865a402828756d9ddf1baa3894e012444d670482d22fce2', 'parallelmesh'],
       'GeomSimAcis': ['51eee6defd24c3cb1837c6db22ff21036586204c0752da3a675358110b7097d2', 'acis'],
       'MeshSim': ['2b7a9b0303ae95c4ac89cf628f6db42ab8b71fe7193736e0ccb4de02b0276241', 'base'],
       'GeomSimAbstract': ['8d9578e94187b4d3a79b03dec8606d525325dfab65b6e73f41acb1dd0494d002', 'abstract'],
       'GeomSimDiscrete': ['9b83735bb2cde1d17699ddc272fe8de2cb6a68c24c51d655ea5856c6c60e9791', 'discrete'],
       'FieldSim': ['55f5cea7425aeab3032bb4a5e22a681272a7e7e5d8a11ffcf93606e3667625be', 'base'],
       }
    },
    {
    'version': '2023.0-230303dev',
    'components': {
       'msparalleladapt': ['91485e2752ee3a10ff937a857213194e1b0e63f729345f077b8dcc9856e3b4f8', 'paralleladapt'],
       'gmabstract': ['6547350c8d52f8546120d9dcce1cf8edf13fbbbc23c7c54a10e01aaa1f9de264', 'abstract'],
       'msadapt': ['a21ce9364ade02c2625372da237bc19446b41c02198e18a56a9d8fdcc328c7e6', 'base'],
       'gmadv': ['578b99405c08c8421a4d24e87c7e11abe3702f182f3b1b55c70e9aa90df81163', 'advmodel'],
       'gmvoxel': ['a0f2c34ab5f8dffd5afee5e30d301f5855840f1eb2727158e30f985636d676bf', 'voxel'],
       'gmcore': ['1b3644f71f1e77714cd043680bf007f37bb7754e9e9757e0daf6565da122b54b', 'base'],
       'pskrnl': ['4a5c00ce59ad1d72b1ed31bb67a8163652ae820e3aea122b6c49e9e1b672b5b7', 'parasolid'],
       'mscore': ['912d4316f4b76193d4c72ffdda91bc2cc75656383dcaaaa0fcc612677171fb8a', 'base'],
       'msparallelmesh': ['2759869bf7534b12620e61328a0b497d39b9ff11c672a33352fa96008f6992e0', 'parallelmesh'],
       'psint': ['c8f0854ec9db10c5bd3c74e2d7c90950055ac08ef72f6b8ae0e2e6ba8e02ab54', 'parasolid'],
       'msadv': ['a19a63c2795d01a2960f62cdf63c3b52f4cb6cadb3a0e166ada624fa8ef90947', 'adv'],
       'fdcore': ['9fb3ddd6b1373fc0e6c32d63cf44c09d5ca7495d11dade60c7088d4b4f6207c2', 'base'],
       'aciskrnl': ['a1363f5d61a84753c53fec7e62dafc6fc01a133f850c1c42bb0f8e50371bfff3', 'acis'],
       'discrete': ['b91016745fa43eba6e5af3686bbe93e4e8b41cbbef1bb89e2e9045406dc78eb5', 'discrete'],
       },
    'docs': {
       'ParallelMeshSimAdapt': ['a32bdb06019684f0ca3fbfc1276c4c80653b83666fe605717ed467cd225b4021', 'paralleladapt'],
       'MeshSimAdapt': ['f3cf6f6973f96108fb381e0f07cf82209440b7f5d65f0ad76acf79d0c458d87e', 'base'],
       'GeomSimParasolid': ['3e72523281dc5e75c993d6e93912a43b25d6420ab8aa755ea715622eba753556', 'parasolid'],
       'GeomSimAdvanced': ['c8265efcbb186b6564d625b28c691bd8dbc98e6e7fdcb59d3b03b6ed2d85d0ba', 'advmodel'],
       'MeshSimAdvanced': ['be5de21e7e217e36672b0ef8d2f61982c11f7858d54cd015ee026d87eb76913d', 'adv'],
       'FieldSim': ['1a7b5c1aefe7ffcbb34fae0378ebc0372f24273c59abc6e521ebae768ecf40c2', 'base'],
       'GeomSim': ['42fe4aca177413b539d5ee5d5afab9d242e363e647042a71a33a0ac0e31a17ae', 'base'],
       'GeomSimVoxel': ['2e2458211a1ef5e68b8cbb1233bf174024feaf6007a08d49723069d11e6b672d', 'voxel'],
       'ParallelMeshSim': ['c534fdf5d014d17da5b18ba52a6bb904b30117258637073e082d680248cd8110', 'parallelmesh'],
       'MeshSim': ['9cf38bb028c4ac205ee8211d0c29ec0b6ff623efc7df37fd7c5a2456045e95c3', 'base'],
       'GeomSimDiscreteModeling': ['139787133702743c0afc8142dad0824e67728501991383092cba56949112df86', 'discrete'],
       'GeomSimDiscrete': ['a7438efa01d11feadda2822b74046ac9e096866625514f8939858cb9056c25cb', 'discrete'],
       'GeomSimAcis': ['a5f94f154ba936740a06b6efbdff9a4f9a4307706b3b9139c579f8de92bea1c4', 'acis'],
       'GeomSimAbstract': ['d47551c4ae8f9693280ec82f0d03f4c26e158006de66d852cd64a77dff8cdd1c', 'abstract'],
       }
    },
    {
    'version': '18.0-220930beta',
    'components': {
        'discrete': ['8d0f15475967e19d0c8d3e07316a9105c18a1cd509b7a86503848ca95372df8c', 'discrete'],
        'gmadv': ['9fb61eebce87020b6cb4934f2c2b42a5c161421062498017053ee84d85c358d4', 'advmodel'],
        'aciskrnl': ['bdc3cc870f716172c8a41bd6fb30b07e66666628b379273a4d722fe93bd87570', 'acis'],
        'msparallelmesh': ['fcad8decb1af2c0c8d8a2503df31589ff83bf7b659ec28fc650312dd7374cf91', 'parallelmesh'],
        'msparalleladapt': ['5a0339defd41358f041a2a899563c7394dedd13f3a435fa0083f357e2d159ba3', 'paralleladapt'],
        'gmcore': ['4ba94be5da5a49e74fce5616cd86389eb5be7205add754837be1920824f11113', 'base'],
        'pskrnl': ['c958315c2ad2c0dd90655ab6a55a7790e0f638eca02c70922f27d73f2a128c31', 'parasolid'],
        'gmvoxel': ['6e1e0d333ca4b4c05aa0ee7837b0a6772e5dc4f451625ba769153c624dfcca0e', 'voxel'],
        'msadapt': ['8ee2a942528d8338242e14b9425c89613fdab38bf3b2a8966bc548038ea7bb81', 'base'],
        'gmabstract': ['6280d0bf496177b5c08a95473241329e0e3637fefa595ff68d053f36c6f4b7ef', 'abstract'],
        'mscore': ['e09bfbb8f8d5c5e2248a72207ab79d90de24d05fd9d093bc458848e5327c4dd6', 'base'],
        'msadv': ['a2aa0b3fea780015eaffc42f72b0daa234dfdf3de9cc5abb661450e24d235754', 'adv'],
        'fdcore': ['0ddd7feb91f3fabe6a6da438616d520b51395a8e8b9e1cf6073e11a3644b89b4', 'base'],
        'psint': ['8d460d12b48d3b2432267fa4182b832b567e252d6e42a937243404fac970ae9f', 'parasolid'],
        },
    'docs': {
        'GeomSim': ['3a00c6a0e37254c8c4e4d94c2ab0eab695a35858a9165c433baf755d265d5af5', 'base'],
        'MeshSimAdapt': ['70bf8c7b6451f9ff0eada8845072250bfdff66c1e6941698c68aa8090fe343b6', 'base'],
        'GeomSimAcis': ['fe6f931581fa1d7489fec7265fbaf7ecb0798836584c7add441cbdb705a69b74', 'acis'],
        'GeomSimAdvanced': ['d504ebb92baf0abb7c0d11b10e975cc90c3d9bd99194801b9654fb3319ea5676', 'advmodel'],
        'MeshSimAdvanced': ['47f790bc94012a2f5c325b7f426f97da0bd12063f8b9f47af1b974702b9564cf', 'adv'],
        'GeomSimAbstract': ['3212083a681cc8517326baecaf8db09fdd2922d2abd9f59769b350901bff1f40', 'abstract'],
        'GeomSimDiscreteModeling': ['de169891a3a81ac83b8536561594f682d04734c50d9488396cc0cf18c65fc39b', 'discrete'],
        'GeomSimDiscrete': ['245b4f00da0542d74c93b21596bcef73991364e886a5035c10f08ae390bca28e', 'discrete'],
        'GeomSimVoxel': ['89689ebf8513e150f697cb44c9fd8d489c4ee2e75c87b90d9985a3ef355757dc', 'voxel'],
        'ParallelMeshSimAdapt': ['47a5d6b5c8e95663d611110e4b6e11404577b4ae6bb2a1403bb0a0b308727b85', 'paralleladapt'],
        'MeshSim': ['5cd6fb69477110b0f63d1b372c3d739b159c7d6d6971e01226eb96cf086735f7', 'base'],
        'GeomSimParasolid': ['55e5a4049adefa54737a52a7ddb60a7c1bf18117362425b8c8258dd408ed2278', 'parasolid'],
        'FieldSim': ['18939b3ca20a48829bb3891f58479a3e36d427251b86d4fc3cf0840802f1f59f', 'base'],
        'ParallelMeshSim': ['4d10a09a5054b1bb554464702826d4486fc27e9453ac015b3107b14e9ca26cdd', 'parallelmesh'],
        }
    },
    {
        "version": "16.0-220312",
        "components": {
            "msparalleladapt": [
                "cc6d6ecba8183f3444e55977af879b297977ff94dd7f6197028110f7e24ea60b",
                "paralleladapt",
            ],
            "msadapt": [
                "ec4a985f9b29914411d299fecfb1a994224070480be5de5f701d9968ba9da9e5",
                "base",
            ],
            "opencascade": [
                "008e7232ee3531b70143129e5a664f7db0e232bad9d11d693d725d39986a8aa4",
                "opencascade",
            ],
            "gmvoxel": [
                "4a74c54c31e9eb93f9a0c09ef3ac88f365efb19666240374aa6d1142db993a2c",
                "voxel",
            ],
            "msadv": ["d33b591147152383130cc2190f1bd7726cb9ea3590468691db3be5815802d888", "adv"],
            "pskrnl": [
                "e154c22c01ecab2e041cf5d87fcb23eab074449dae7f677f17e7863b6da70fdc",
                "parasolid",
            ],
            "gmcore": ["d9ed89d07d83f2c23eca6a27fd9000fd4c8eeefa70ac860aa28a40000a6ec93e", "base"],
            "psint": [
                "5c236e429f28a36a36cb09ec3f4778dc7b6e72447014b684792eea733bb21fd5",
                "parasolid",
            ],
            "msparallelmesh": [
                "a791f4464da54faafdc63dbcaf3d326ffc49c9ea8d53e36cc57c15607cf72db9",
                "parallelmesh",
            ],
            "mscore": ["48e367e476a03a9fa5389830a6c60824b5d620d04d87392e423a33a331ba3595", "base"],
            "fdcore": ["022de14021434d90daee8ea1200c024d98a7eb01bb9cb5a06a3b2f7ffee9c0a1", "base"],
            "gmadv": [
                "6232ec08ef5cff4269d066b035490f33c199fb545355836ef1536b1a00179b2c",
                "advmodel",
            ],
            "gmabstract": [
                "08a6c7423ed59361c5330dbe00b8914d1d55160de73002e7e552c45c8316f37a",
                "abstract",
            ],
            "discrete": [
                "f5ae00688cf202e75686955185d95952e7b581b414dd52bfef0d917e5959ab22",
                "discrete",
            ],
            "aciskrnl": [
                "c2c7b0c495d47a5662765f1b0c6f52863032e63384d85241e6313c4b773e9ed2",
                "acis",
            ],
        },
        "docs": {
            "GeomSimParasolid": [
                "3420fcc1ac67cff8f46b79553cfe478f34676b9b0cd1fa913255b48cbdfd6ad4",
                "parasolid",
            ],
            "GeomSimAcis": [
                "77b31bfb368f1e7981b3a81087e4e287c560e0a0cd08920b36dc81fea25bcdfa",
                "acis",
            ],
            "MeshSimAdvanced": [
                "abeeb0cb10cf3074295a880412e0568b653f2784b1de19f0f8ede5eec536a8bd",
                "adv",
            ],
            "GeomSim": [
                "b1e762111eb8025b966b0aca4bef3768325d9f1c1e3c72a1246b59539e444eb2",
                "base",
            ],
            "GeomSimVoxel": [
                "bc43f931670657a2cae79f9a2a02048b511fa6e405f15e583631e9f6888e7000",
                "voxel",
            ],
            "ParallelMeshSimAdapt": [
                "dd3a0fd6b889dadb45f9a894f684353fffa25bf15be60ae8e09d0c035045e192",
                "paralleladapt",
            ],
            "GeomSimAdvanced": [
                "3e971ae069baf94b38794318f97f16dc25cf50f6a81413903fbe17407cbd73b3",
                "advmodel",
            ],
            "GeomSimGranite": [
                "e438c19bb94a182068bf327988bd1ff9c1e391876cd9b7c74760b98cbfd08763",
                "granite",
            ],
            "FieldSim": [
                "5ede572cbb7539921482390e5890daa92399a5f1ee68a98d3241a7d062667d9d",
                "base",
            ],
            "MeshSimAdapt": [
                "c4be287da651c68e246034b28e141143d83fc3986fd680174a0d6de7b1cc35ab",
                "base",
            ],
            "GeomSimOpenCascade": [
                "34a8d628d07ab66159d6151276e93fdabfcc92a370f5927b66a71d3a8545652c",
                "opencascade",
            ],
            "GeomSimDiscrete": [
                "d2b11367334401ec57390a658715e91bbf3e3a0e8521fab1ad5d3f7c215b2921",
                "discrete",
            ],
            "GeomSimAbstract": [
                "601b0179b65a385a39d241a9a4e3074e4f834c817e836bea07516015c769e666",
                "abstract",
            ],
            "GeomSimDiscreteModeling": [
                "619b8254d8e3bcc94e84551e997b577dd9325131d084c3b3693ab665b7e4213b",
                "discrete",
            ],
            "ParallelMeshSim": [
                "5b74b9b5f9290111366e341c12d4777635e375523d42cb0a2b24aa1bfa8ab8c4",
                "parallelmesh",
            ],
            "MeshSim": [
                "2f1944e1853a550cc474201790555212e4b7a21d3675715de416718a789ccae2",
                "base",
            ],
        },
    },
    {
        "version": "16.0-210623",
        "components": {
            "gmadv": [
                "c40dac44695db6e97c4d4c06d1eb6eac93518c93d7860c77a69f3ea30fea3b90",
                "advmodel",
            ],
            "msparallelmesh": [
                "57d710b74887731ea0e664a154489747033af433852809181c11e8065752eaf4",
                "parallelmesh",
            ],
            "gmcore": ["5bd04f175fdf5a088140af5ca3fa03934251c097044b47fdf3ea2cd0afc28547", "base"],
            "pskrnl": [
                "87957818b20839d3835a343894c396f7c591d1f0bfd728d33ad21b1adb4e887c",
                "parasolid",
            ],
            "msadapt": [
                "5ba66819bb2c56eb1e07e6c2659afc8c971005b08ed059f8c62a185236e45dac",
                "base",
            ],
            "gmvoxel": [
                "15dfc389665086ea37b9835fecd6b46070572878308796afa960077cc2bf7e0a",
                "voxel",
            ],
            "msparalleladapt": [
                "1db2c34a398c5965a2a675006c96a3603e0124188b52159776b7c616efa48457",
                "paralleladapt",
            ],
            "mscore": ["7029871c52d6c3bb782ae2acb7360130105649cd9cf63815ae95cf4089cb786d", "base"],
            "psint": [
                "c8a3dbacafa70b13bc9fb8322699a1cfc812b2cfd3ea05cba9135623eae761d8",
                "parasolid",
            ],
            "fdcore": ["75f9bcd7cb9ab9dedb73166539c08b53bd8e91c5619d3dce605ba19c63d1ee5c", "base"],
            "msadv": ["0018e0a6b9d7724867f7379bc619269481c318ee4dfd0724511c032534ae04a1", "adv"],
            "aciskrnl": [
                "2a9b9da9b0c09857de7fef0dea0e96222bd30e297bd37bea962751dab6762500",
                "acis",
            ],
            "discrete": [
                "f17cd198f8749c763cc8e200cfd6734604e1d316a48d7d0e537a9a890d884904",
                "discrete",
            ],
            "gmabstract": [
                "068d0309d5ff9668fc0474edf7f4e20503827400e34492e2ed55b46a0c9e1858",
                "abstract",
            ],
        },
        "docs": {
            "GeomSimAdvanced": [
                "02e4566042ae4de10c4acb577142e82d15f32caa296fe1b578c62a38da707066",
                "advmodel",
            ],
            "MeshSim": [
                "cc1dc77cece7aac6ded003c872c651ad8321bc9ce931ad141b17d2de7bf513c5",
                "base",
            ],
            "GeomSimVoxel": [
                "49b8f85f59acc8c973bf46c1f999a0ae64cdf129371587879de056c0ac3500d8",
                "voxel",
            ],
            "MeshSimAdvanced": [
                "2d2689979104414d91d804ca3c34a69104e572b8f231c4e324b09e57675b61cc",
                "adv",
            ],
            "GeomSimGranite": [
                "17f18831a12b06c0e085486d94d3a4275d7ed94ad53fec689e8877217856c750",
                "granite",
            ],
            "GeomSimParasolid": [
                "492bd311cc42dadd1f76064c57d35e886b9a7da4c48576ec4d34844fcdaddb8d",
                "parasolid",
            ],
            "GeomSimAcis": [
                "341c6aeda7f9189f4e886cb75c5989cb9ece6ecba1b1c9d5273b94f74a3dd40b",
                "acis",
            ],
            "GeomSimDiscrete": [
                "e9d42da613a3acadbcdee5d8d6fc3b093f58b51d158f2a392b7da0e5f74e0388",
                "discrete",
            ],
            "MeshSimAdapt": [
                "e27510e588105bdb0ca62c2629dfd41dfca6039b7b2ff0298ef83d3a48d7dd23",
                "base",
            ],
            "GeomSimAbstract": [
                "398c1a15efcddd3b86a7b0334af6f8b529710f815f73f5655d3c7271e92b194e",
                "abstract",
            ],
            "GeomSimDiscreteModeling": [
                "f444aed59569731f65eea920322adcc224c67b715ecba85a1898cf418de58237",
                "discrete",
            ],
            "FieldSim": [
                "bac947998d4de1c4edba271645310d4784290bec30bf0cf41d00ae6ea8b27c97",
                "base",
            ],
            "GeomSim": [
                "95cb24165d47701daa8da7131ca1173d38f4dab80c1ca0d75843b464fed92097",
                "base",
            ],
            "ParallelMeshSim": [
                "fb1e3ac0ab7208d771057880c693e529e7c821772265b89125d371a1b34fa651",
                "parallelmesh",
            ],
            "ParallelMeshSimAdapt": [
                "246c5c8b30194239f41a79f2ffd205fd9ae69bcb8127d19a94f12c278a27f106",
                "paralleladapt",
            ],
        },
    },
    {
        "version": "14.0-191122",
        "components": {
            "gmadv": [
                "01cea5f7aff5e442ea544df054969740ad33e2ff4097cf02de31874d16a0c7c2",
                "advmodel",
            ],
            "msadapt": [
                "69839698f24969f97963869fd212bdcff0b5d52dd40ec3fdc710d878e43b527a",
                "base",
            ],
            "gmvoxel": [
                "bfea15e1fc5d258ed9db69132042a848ca81995e92bf265215e4b88d08a308a8",
                "voxel",
            ],
            "gmabstract": [
                "dccdcd4b71758e4110cd69b0befa7875e5c1f3871f87478410c6676da3f39092",
                "abstract",
            ],
            "fdcore": ["6981b2eb0c0143e6abc3ec29918fc3552f81018755770bf922d2491275984e1a", "base"],
            "msparallelmesh": [
                "1e1a431ec9dd85354ff42c6a2a41df7fbe3dfe5d296f40105c4d3aa372639dc3",
                "parallelmesh",
            ],
            "mscore": ["bca80fcb2c86e7b6dc0259681ccd73197ce85c47f00f1910bd6b518fa0b3a092", "base"],
            "discrete": [
                "430e5f2270864b1ab9c8dff75d2510147a0c5cde8af0828975d9e38661be3a35",
                "discrete",
            ],
            "gmimport": [
                "e83b3c43b7c695fa96ed42253a4b317a2882bcb8987fd3225c09492e353e49aa",
                "import",
            ],
            "pskrnl": [
                "31455cfce746b2339b3644f3890d4444014fb839654a9f576ec747d28ff6c1c4",
                "parasolid",
            ],
            "gmcore": ["af5d89b9ce266cac5b45f2bf96e1324e87e54c6e2f568bd5b6a85c41122d39e4", "base"],
            "aciskrnl": [
                "764e5633e6d502951788accfb8c34ed59430a4779a44d1775fd67f9aab8a654a",
                "acis",
            ],
            "msparalleladapt": [
                "8ae607112958f6b9d319736c71a6597cf99a8a59ceed733f2a939cb9cfa6dd67",
                "paralleladapt",
            ],
            "psint": [
                "f6c90b2fe87e690b2cba20f357d03c5962fed91541d6b79e01dc25cb8f01d1e0",
                "parasolid",
            ],
            "msadv": ["f18a8285d539cb07b00fde06fe970d958eceabf2a10182bcca6c8ad1c074c395", "adv"],
        },
        "docs": {
            "MeshSim": [
                "f3c475072f270ff49ac2f6639ca1cddb0642889648cbea7df1a3f1b85f7cac36",
                "base",
            ],
            "GeomSimVoxel": [
                "9f4ee5a8204fee1d899cb912e0379f8be7a826e81ca0a0d8a670a4b804ca1276",
                "voxel",
            ],
            "MeshSimAdvanced": [
                "8c8bc3709238e600e8938c7c345588f8947d89eae98a228b0d0e3d46f5f4c0d9",
                "adv",
            ],
            "GeomSimDiscreteModeling": [
                "4e8e26a88e8a5ad396a637597a52f5973d8f77abc0a5b99fa737caf37226d6cc",
                "discrete",
            ],
            "GeomSimAdvanced": [
                "5efb38317d6be7862ce34024922ca372b30691a30af820474e2e26e4c3055278",
                "advmodel",
            ],
            "GeomSimParasolid": [
                "6851bdaf6d96e7b2335fce3394825e9876800f0aba0a42644758dc1bd06f60fe",
                "parasolid",
            ],
            "GeomSimImport": [
                "d931ecfc332460c825b473c0950c7ae8ff9f845e0d1565f85bfd7698da5e6d26",
                "import",
            ],
            "ParallelMeshSim": [
                "0f0d235b25a660271e401488e412220f574b341dadb827f7b82f0e93172b5cdb",
                "parallelmesh",
            ],
            "ParallelMeshSimAdapt": [
                "7964ebbd7e8d971ea85fc5260e44f7e876da5ad474dc67d8d6fc939bfa5ba454",
                "paralleladapt",
            ],
            "GeomSimAcis": [
                "dea82efbc4e3043ecda163be792ef295057e08be17654a7783ce7ca5e786f950",
                "acis",
            ],
            "MeshSimAdapt": [
                "ee4d5595572c1fe1a0d78bd9b85c774a55e994c48170450d6c5f34b05fcf2411",
                "base",
            ],
            "FieldSim": [
                "6b09b4ab278911d3e9229fd4cd8dc92ba188f151d42d9d7b96d542aad2af1fac",
                "base",
            ],
            "GeomSim": [
                "0673823d649998367c0e427055911eae971bb6e8c76625882e7a7901f4d18c44",
                "base",
            ],
            "GeomSimDiscrete": [
                "58dfd33fc5cdd2ab24e9084377943f28d5ba68b8c017b11b71cde64c5e4f2113",
                "discrete",
            ],
            "GeomSimAbstract": [
                "16248cd2a0d133029eb4b79d61397da008e4d5b5c3eaf0161a0a44148b0bc519",
                "abstract",
            ],
        }
        },
        {
            'version': '16.0-210623',
            'components': {
                'gmadv': ['c40dac44695db6e97c4d4c06d1eb6eac93518c93d7860c77a69f3ea30fea3b90', 'advmodel'],
                'msparallelmesh': ['57d710b74887731ea0e664a154489747033af433852809181c11e8065752eaf4', 'parallelmesh'],
                'gmcore': ['5bd04f175fdf5a088140af5ca3fa03934251c097044b47fdf3ea2cd0afc28547', 'base'],
                'pskrnl': ['87957818b20839d3835a343894c396f7c591d1f0bfd728d33ad21b1adb4e887c', 'parasolid'],
                'msadapt': ['5ba66819bb2c56eb1e07e6c2659afc8c971005b08ed059f8c62a185236e45dac', 'base'],
                'gmvoxel': ['15dfc389665086ea37b9835fecd6b46070572878308796afa960077cc2bf7e0a', 'voxel'],
                'msparalleladapt': ['1db2c34a398c5965a2a675006c96a3603e0124188b52159776b7c616efa48457', 'paralleladapt'],
                'mscore': ['7029871c52d6c3bb782ae2acb7360130105649cd9cf63815ae95cf4089cb786d', 'base'],
                'psint': ['c8a3dbacafa70b13bc9fb8322699a1cfc812b2cfd3ea05cba9135623eae761d8', 'parasolid'],
                'fdcore': ['75f9bcd7cb9ab9dedb73166539c08b53bd8e91c5619d3dce605ba19c63d1ee5c', 'base'],
                'msadv': ['0018e0a6b9d7724867f7379bc619269481c318ee4dfd0724511c032534ae04a1', 'adv'],
                'aciskrnl': ['2a9b9da9b0c09857de7fef0dea0e96222bd30e297bd37bea962751dab6762500', 'acis'],
                'discrete': ['f17cd198f8749c763cc8e200cfd6734604e1d316a48d7d0e537a9a890d884904', 'discrete'],
                'gmabstract': ['068d0309d5ff9668fc0474edf7f4e20503827400e34492e2ed55b46a0c9e1858', 'abstract'],
            },
            'docs': {
                'GeomSimAdvanced': ['02e4566042ae4de10c4acb577142e82d15f32caa296fe1b578c62a38da707066', 'advmodel'],
                'MeshSim': ['cc1dc77cece7aac6ded003c872c651ad8321bc9ce931ad141b17d2de7bf513c5', 'base'],
                'GeomSimVoxel': ['49b8f85f59acc8c973bf46c1f999a0ae64cdf129371587879de056c0ac3500d8', 'voxel'],
                'MeshSimAdvanced': ['2d2689979104414d91d804ca3c34a69104e572b8f231c4e324b09e57675b61cc', 'adv'],
                'GeomSimGranite': ['17f18831a12b06c0e085486d94d3a4275d7ed94ad53fec689e8877217856c750', 'granite'],
                'GeomSimParasolid': ['492bd311cc42dadd1f76064c57d35e886b9a7da4c48576ec4d34844fcdaddb8d', 'parasolid'],
                'GeomSimAcis': ['341c6aeda7f9189f4e886cb75c5989cb9ece6ecba1b1c9d5273b94f74a3dd40b', 'acis'],
                'GeomSimDiscrete': ['e9d42da613a3acadbcdee5d8d6fc3b093f58b51d158f2a392b7da0e5f74e0388', 'discrete'],
                'MeshSimAdapt': ['e27510e588105bdb0ca62c2629dfd41dfca6039b7b2ff0298ef83d3a48d7dd23', 'base'],
                'GeomSimAbstract': ['398c1a15efcddd3b86a7b0334af6f8b529710f815f73f5655d3c7271e92b194e', 'abstract'],
                'GeomSimDiscreteModeling': ['f444aed59569731f65eea920322adcc224c67b715ecba85a1898cf418de58237', 'discrete'],
                'FieldSim': ['bac947998d4de1c4edba271645310d4784290bec30bf0cf41d00ae6ea8b27c97', 'base'],
                'GeomSim': ['95cb24165d47701daa8da7131ca1173d38f4dab80c1ca0d75843b464fed92097', 'base'],
                'ParallelMeshSim': ['fb1e3ac0ab7208d771057880c693e529e7c821772265b89125d371a1b34fa651', 'parallelmesh'],
                'ParallelMeshSimAdapt': ['246c5c8b30194239f41a79f2ffd205fd9ae69bcb8127d19a94f12c278a27f106', 'paralleladapt'],
            }
        },
        {
            'version': '14.0-191122',
            'components': {
                'gmadv': ['01cea5f7aff5e442ea544df054969740ad33e2ff4097cf02de31874d16a0c7c2', 'advmodel'],
                'msadapt': ['69839698f24969f97963869fd212bdcff0b5d52dd40ec3fdc710d878e43b527a', 'base'],
                'gmvoxel': ['bfea15e1fc5d258ed9db69132042a848ca81995e92bf265215e4b88d08a308a8', 'voxel'],
                'gmabstract': ['dccdcd4b71758e4110cd69b0befa7875e5c1f3871f87478410c6676da3f39092', 'abstract'],
                'fdcore': ['6981b2eb0c0143e6abc3ec29918fc3552f81018755770bf922d2491275984e1a', 'base'],
                'msparallelmesh': ['1e1a431ec9dd85354ff42c6a2a41df7fbe3dfe5d296f40105c4d3aa372639dc3', 'parallelmesh'],
                'mscore': ['bca80fcb2c86e7b6dc0259681ccd73197ce85c47f00f1910bd6b518fa0b3a092', 'base'],
                'discrete': ['430e5f2270864b1ab9c8dff75d2510147a0c5cde8af0828975d9e38661be3a35', 'discrete'],
                'gmimport': ['e83b3c43b7c695fa96ed42253a4b317a2882bcb8987fd3225c09492e353e49aa', 'import'],
                'pskrnl': ['31455cfce746b2339b3644f3890d4444014fb839654a9f576ec747d28ff6c1c4', 'parasolid'],
                'gmcore': ['af5d89b9ce266cac5b45f2bf96e1324e87e54c6e2f568bd5b6a85c41122d39e4', 'base'],
                'aciskrnl': ['764e5633e6d502951788accfb8c34ed59430a4779a44d1775fd67f9aab8a654a', 'acis'],
                'msparalleladapt': ['8ae607112958f6b9d319736c71a6597cf99a8a59ceed733f2a939cb9cfa6dd67', 'paralleladapt'],
                'psint': ['f6c90b2fe87e690b2cba20f357d03c5962fed91541d6b79e01dc25cb8f01d1e0', 'parasolid'],
                'msadv': ['f18a8285d539cb07b00fde06fe970d958eceabf2a10182bcca6c8ad1c074c395', 'adv'],
            },
            'docs': {
                'MeshSim': ['f3c475072f270ff49ac2f6639ca1cddb0642889648cbea7df1a3f1b85f7cac36', 'base'],
                'GeomSimVoxel': ['9f4ee5a8204fee1d899cb912e0379f8be7a826e81ca0a0d8a670a4b804ca1276', 'voxel'],
                'MeshSimAdvanced': ['8c8bc3709238e600e8938c7c345588f8947d89eae98a228b0d0e3d46f5f4c0d9', 'adv'],
                'GeomSimDiscreteModeling': ['4e8e26a88e8a5ad396a637597a52f5973d8f77abc0a5b99fa737caf37226d6cc', 'discrete'],
                'GeomSimAdvanced': ['5efb38317d6be7862ce34024922ca372b30691a30af820474e2e26e4c3055278', 'advmodel'],
                'GeomSimParasolid': ['6851bdaf6d96e7b2335fce3394825e9876800f0aba0a42644758dc1bd06f60fe', 'parasolid'],
                'GeomSimImport': ['d931ecfc332460c825b473c0950c7ae8ff9f845e0d1565f85bfd7698da5e6d26', 'import'],
                'ParallelMeshSim': ['0f0d235b25a660271e401488e412220f574b341dadb827f7b82f0e93172b5cdb', 'parallelmesh'],
                'ParallelMeshSimAdapt': ['7964ebbd7e8d971ea85fc5260e44f7e876da5ad474dc67d8d6fc939bfa5ba454', 'paralleladapt'],
                'GeomSimAcis': ['dea82efbc4e3043ecda163be792ef295057e08be17654a7783ce7ca5e786f950', 'acis'],
                'MeshSimAdapt': ['ee4d5595572c1fe1a0d78bd9b85c774a55e994c48170450d6c5f34b05fcf2411', 'base'],
                'FieldSim': ['6b09b4ab278911d3e9229fd4cd8dc92ba188f151d42d9d7b96d542aad2af1fac', 'base'],
                'GeomSim': ['0673823d649998367c0e427055911eae971bb6e8c76625882e7a7901f4d18c44', 'base'],
                'GeomSimDiscrete': ['58dfd33fc5cdd2ab24e9084377943f28d5ba68b8c017b11b71cde64c5e4f2113', 'discrete'],
                'GeomSimAbstract': ['16248cd2a0d133029eb4b79d61397da008e4d5b5c3eaf0161a0a44148b0bc519', 'abstract'],
            }
        },
        {
            'version': '12.0-191027',
            'components': {
                'gmadv': ['1a133523062974c4d9acb1d52baa3893dc891482aebaaeb79a7dc907461d5dbc', 'advmodel'],
                'fdcore': ['c3a89093f811cb489698d203dbe68ca910e6c67ea75c0a7aba73dd369508b9ec', 'base'],
                'mscore': ['a2f043278d45d8729020b663c66c57960fcec33dafd3d90db55f0a9e32723bce', 'base'],
                'msparallelmesh': ['2f6fd47d3c5c2f1ece4634985a522ac599d3cee20ad8a4623f252cc75aa32c4c', 'parallelmesh'],
                'msparalleladapt': ['8d288730b1300215a32f3b21624bd2e0e2d8a684fe928459757fcec7e0aeb7d3', 'paralleladapt'],
                'gmabstract': ['3b608f21e6c11db5bb48e49f9cd7e9d88aeec4feadebd778529a5c9d506d08c6', 'abstract'],
                'gmimport': ['fc1626c7b1522b90eaa3926e1253b84d28440c7df8634decdedb79b5229be800', 'import'],
                'discrete': ['a15ead08138f0c59c7ee46cd0d348d4f26e1b021d2580a134cf2b84a7337bcf9', 'discrete'],
                'aciskrnl': ['8773f00e08d237052c877e79d1a869214f59891e812d70df938b2a5e5423a96f', 'acis'],
                'msadv': ['41bdb9555ab9feb0891f0832a49fc29777d40957473f315e1c33e1c0077cba7d', 'adv'],
                'psint': ['b040ab48833eb2a748f757e2de6929f3002aa98db459ba92bd9a88e443e5cb07', 'parasolid'],
                'gmvoxel': ['19fba83c9c7eac20d9613236530fbae652dc8edef35233214f0f92b81c91a877', 'voxel'],
                'msadapt': ['1a752adb6724c3328fffb26f1aebed007d3c2a5df725cd29aa0cf0fdfda1f39a', 'base'],
                'gmcore': ['ec95bae84b36644e6e04cf0a6b4e813a51990d0a30519176ebb8a05f681af7f2', 'base'],
                'pskrnl': ['7b7b4952513e06c8c23aa8f7c1748f5c199d9af70ea06c4a359412237ed8ac1d', 'parasolid'],
            },
            'docs': {
                'FieldSim': ['5109d91fe61ccdaf0af5aa869aea9c38ec98760746ec3983d100f870cbb1cb63', 'base'],
                'ParallelMeshSim': ['a1e6618a77022a9580beac4c698dd4b9aa70f617a27db9ce13ab1f2388475290', 'parallelmesh'],
                'GeomSimAcis': ['f0319b32eb417fa9b237575d9b2dc1c061848888c36fd4da97d97cdbb3cf19c3', 'acis'],
                'GeomSimAbstract': ['c44023e6944522057c47925db49089031c7de9b67938ca6a987e04fadfeda9b7', 'abstract'],
                'GeomSimDiscrete': ['ad648752fa7d2dc1ce234a612e28ce84eb1f064a1decadf17b42e9fe56967350', 'discrete'],
                'MeshSimAdapt': ['dcb7d6ec74c910b41b5ae707d9fd4664fcb3a0fdb2c876caaa28a6f1cf701024', 'base'],
                'MeshSim': ['e5a8cb300b1e13b9f2733bf8b738872ffb37d9df15836a6ab264483c10000696', 'base'],
                'GeomSimParasolid': ['2bf33cc5b3879716437d45fde0a02caaa165e37d248d05b4b00708e76573a15e', 'parasolid'],
                'GeomSimImport': ['5309433dcdce660e062412f070719eefcc6299764e9b0169533ff343c9c9c406', 'import'],
                'ParallelMeshSimAdapt': ['2e8e0ceede3107b85dba9536f3bbf5e6959793073a5147548cfb01ca568c8da2', 'paralleladapt'],
                'GeomSimDiscreteModeling': ['ff88ec234b890315cc36539e3f73f4f977dab94160860950e7b7ee0303c9b55e', 'discrete'],
                'GeomSim': ['62ae33372f999d5e62a1b7b161ddd7de04c055adc85cfd258e088c95b76d5fef', 'base'],
                'GeomSimVoxel': ['7a624ddaebd833077511acac3efd4b4c1dab09bd9feff40aba0813182eeb262f', 'voxel'],
                'GeomSimAdvanced': ['f0ab801ddf3d701a4ac3f8c47900cc858a4488eb0fe2f663504ba260cd270d20', 'advmodel'],
                'MeshSimAdvanced': ['bb532027e4fcc311a7c376383da010aed5ee133a9122b186a4e5c7d0cf1d976b', 'adv'],
            }
        }
    ]


def simmetrix_makecomponenturl(name):
    """only supporting the linux libraries"""
    prefix = "file://{0}/".format(os.getcwd())
    suffix = "-" + "linux64.tgz"
    return prefix + name + suffix


def simmetrix_makedocurl(name):
    """doc zip files are not os/arch specific"""
    prefix = "file://{0}/".format(os.getcwd())
    suffix = '.zip'
    return prefix + name + suffix


def simmetrix_setkernelcmakeprefixpath(spec, path, env):
    if '+acis' in spec:
        env.append_path('CMAKE_PREFIX_PATH', join_path(path, 'acisKrnl'))
        env.append_path('LD_LIBRARY_PATH', join_path(path, 'acisKrnl'))
    if '+parasolid' in spec:
        env.append_path('CMAKE_PREFIX_PATH', join_path(path, 'psKrnl'))
        env.append_path('LD_LIBRARY_PATH', join_path(path, 'psKrnl'))


def simmetrix_resource(name, url, sha256, condition):
    # The tarballs/zips each have the same directory structure.  Because of
    # this, and the bug in spack described here:
    # https://github.com/spack/spack/pull/3553#issuecomment-391424244
    # , they cannot be expanded into the source root directory.
    # Once this is fixed the 'destination=name' argument can be removed.
    resource(
        name=name,
        url=url,
        sha256=sha256,
        destination=name,
        when=condition
    )


class SimmetrixSimmodsuite(Package):
    """Simmetrix' Simulation Modeling Suite is a set of component software
    toolkits that allow developers to easily implement geometry-based
    simulation applications.
    Each component of the Simulation Modeling Suite is designed to address
    specific capabilities:
    | MeshSim - automatic mesh generation
    | FieldSim - simulation data management
    | GeomSim - direct, untranslated access to geometry from a wide variety
    of sources
    """

    maintainers = ['cwsmith']
    homepage = "http://www.simmetrix.com/products/SimulationModelingSuite/main.html"
    manual_download = True

    license_required = True
    license_vars     = ['SIM_LICENSE_FILE']

    variant("base", default=True, description="enable the base components")
    variant("crack", default=True, description="enable the meshsim crack components")
    variant("advmodel", default=False, description="enable advaced modeling")
    variant("abstract", default=False, description="enable abstract modeling")
    variant("voxel", default=False, description="enable voxel modeling")
    variant("discrete", default=False, description="enable discrete modeling")
    variant("acis", default=False, description="enable acis modeling")
    variant("parasolid", default=False, description="enable parasolid modeling")
    variant(
        "opencascade",
        default=False,
        when="@16.0-220312:",
        description="enable opencascade modeling",
    )
    variant("granite", default=False, description="enable granite modeling")
    variant("import", default=False, description="enable import modeling")
    variant("adv", default=False, description="enable advanced meshing")
    variant("parallelmesh", default=False, description="enable parallel meshing")
    variant("paralleladapt", default=False, description="enable parallel adaptation")

    depends_on('mpi')

    oslib = 'x64_rhel7_gcc48'

    for release in RELEASES:
        # define the version using the mscore tarball
        sim_version = release['version']
        main_pkg_name = 'mscore'
        url = simmetrix_makecomponenturl(main_pkg_name)
        sha256 = release['components'][main_pkg_name][0]
        version(sim_version, sha256=sha256, url=url)
        # define resources for the other tarballs
        for name, atts in release['components'].items():
            # skip the tarball used for the version(...) call
            if name == 'mscore':
                continue
            sha256 = atts[0]
            feature = atts[1]
            url = simmetrix_makecomponenturl(name)
            condition = "@{0}+{1}".format(sim_version, feature)
            simmetrix_resource(name, url, sha256, condition)
        # define resources for the document zip files
        for name, atts in release['docs'].items():
            sha256 = atts[0]
            feature = atts[1]
            url = simmetrix_makedocurl(name)
            condition = "@{0}+{1}".format(sim_version, feature)
            simmetrix_resource(name, url, sha256, condition)

    def setup_dependent_build_environment(self, env, dependent_spec):
        archlib = join_path(prefix.lib, self.oslib)
        env.append_path('CMAKE_PREFIX_PATH', archlib)
        simmetrix_setkernelcmakeprefixpath(self.spec, archlib, env)

    def setup_run_environment(self, env):
        archlib = join_path(prefix.lib, self.oslib)
        env.append_path('CMAKE_PREFIX_PATH', archlib)
        simmetrix_setkernelcmakeprefixpath(self.spec, archlib, env)

    def install(self, spec, prefix):
        if not spec.satisfies('platform=linux'):
            raise InstallError('Only the linux platform is supported')
        source_path = self.stage.source_path
        for release in RELEASES:
            simversion = release['version']
            if simversion != spec.version.string:
                continue
            for name, atts in release['components'].items():
                feature = atts[1]
                if '+' + feature in spec:
                    if name == 'mscore':
                        install_tree(join_path(source_path, 'lib'), prefix.lib)
                        install_tree(
                            join_path(source_path, 'include'),
                            prefix.include)
                    else:
                        path = join_path(
                            source_path,
                            name,
                            self.version.string)
                        install_tree(path, prefix)
            for name, atts in release['docs'].items():
                feature = atts[1]
                if '+' + feature in spec:
                    path = join_path(
                        source_path,
                        name,
                        self.version.string)
                    install_tree(path, prefix)

        workdir = prefix.code.PartitionWrapper
        if '+parallelmesh' in spec:
            with working_dir(workdir):
                mpi_id = spec['mpi'].name + spec['mpi'].version.string
                # build the wrapper lib
                make("-f", "Makefile.custom",
                     "CC=%s" % spec['mpi'].mpicc,
                     "CXX=%s" % spec['mpi'].mpicxx,
                     "PARALLEL=%s" % mpi_id,
                     "PQUAL=-%s" % mpi_id,
                     "OPTFLAGS=-O2 -DNDEBUG " + self.compiler.cc_pic_flag)
                libname = 'libSimPartitionWrapper-' + mpi_id + '.a'
                wrapperlibpath = join_path(workdir, 'lib', libname)
                install(wrapperlibpath, join_path(prefix.lib, self.oslib))
