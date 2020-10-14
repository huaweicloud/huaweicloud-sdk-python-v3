# coding: utf-8

import pprint
import re

import six





class CreateThumbReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'input': 'ObsObjInfo',
        'output': 'ObsObjInfo',
        'user_data': 'str',
        'thumbnail_para': 'ThumbnailPara',
        'tar': 'int',
        'sync': 'int',
        'original_dir': 'int',
        'project_id': 'str',
        'tenant_project_id': 'str',
        'domain_name': 'str',
        'canonical_grant_id': 'str'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output',
        'user_data': 'user_data',
        'thumbnail_para': 'thumbnail_para',
        'tar': 'tar',
        'sync': 'sync',
        'original_dir': 'original_dir',
        'project_id': 'project_id',
        'tenant_project_id': 'tenant_project_id',
        'domain_name': 'domain_name',
        'canonical_grant_id': 'canonical_grant_id'
    }

    def __init__(self, input=None, output=None, user_data=None, thumbnail_para=None, tar=1, sync=0, original_dir=0, project_id=None, tenant_project_id=None, domain_name=None, canonical_grant_id=None):
        """CreateThumbReq - a model defined in huaweicloud sdk"""
        
        

        self._input = None
        self._output = None
        self._user_data = None
        self._thumbnail_para = None
        self._tar = None
        self._sync = None
        self._original_dir = None
        self._project_id = None
        self._tenant_project_id = None
        self._domain_name = None
        self._canonical_grant_id = None
        self.discriminator = None

        self.input = input
        self.output = output
        if user_data is not None:
            self.user_data = user_data
        self.thumbnail_para = thumbnail_para
        if tar is not None:
            self.tar = tar
        if sync is not None:
            self.sync = sync
        if original_dir is not None:
            self.original_dir = original_dir
        if project_id is not None:
            self.project_id = project_id
        if tenant_project_id is not None:
            self.tenant_project_id = tenant_project_id
        if domain_name is not None:
            self.domain_name = domain_name
        if canonical_grant_id is not None:
            self.canonical_grant_id = canonical_grant_id

    @property
    def input(self):
        """Gets the input of this CreateThumbReq.


        :return: The input of this CreateThumbReq.
        :rtype: ObsObjInfo
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateThumbReq.


        :param input: The input of this CreateThumbReq.
        :type: ObsObjInfo
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CreateThumbReq.


        :return: The output of this CreateThumbReq.
        :rtype: ObsObjInfo
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateThumbReq.


        :param output: The output of this CreateThumbReq.
        :type: ObsObjInfo
        """
        self._output = output

    @property
    def user_data(self):
        """Gets the user_data of this CreateThumbReq.

        用户自定义数据。 

        :return: The user_data of this CreateThumbReq.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateThumbReq.

        用户自定义数据。 

        :param user_data: The user_data of this CreateThumbReq.
        :type: str
        """
        self._user_data = user_data

    @property
    def thumbnail_para(self):
        """Gets the thumbnail_para of this CreateThumbReq.


        :return: The thumbnail_para of this CreateThumbReq.
        :rtype: ThumbnailPara
        """
        return self._thumbnail_para

    @thumbnail_para.setter
    def thumbnail_para(self, thumbnail_para):
        """Sets the thumbnail_para of this CreateThumbReq.


        :param thumbnail_para: The thumbnail_para of this CreateThumbReq.
        :type: ThumbnailPara
        """
        self._thumbnail_para = thumbnail_para

    @property
    def tar(self):
        """Gets the tar of this CreateThumbReq.

        是否压缩抽帧图片生成tar包。  取值如下：  - 0：压缩。 - 1：不压缩 

        :return: The tar of this CreateThumbReq.
        :rtype: int
        """
        return self._tar

    @tar.setter
    def tar(self, tar):
        """Sets the tar of this CreateThumbReq.

        是否压缩抽帧图片生成tar包。  取值如下：  - 0：压缩。 - 1：不压缩 

        :param tar: The tar of this CreateThumbReq.
        :type: int
        """
        self._tar = tar

    @property
    def sync(self):
        """Gets the sync of this CreateThumbReq.

        是否同步处理，同步处理是指不下载全部文件，快速定位到截图位置进行截图。  取值如下： - 0：排队处理。 - 1：同步处理，暂只支持按时间点截单张图。 

        :return: The sync of this CreateThumbReq.
        :rtype: int
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        """Sets the sync of this CreateThumbReq.

        是否同步处理，同步处理是指不下载全部文件，快速定位到截图位置进行截图。  取值如下： - 0：排队处理。 - 1：同步处理，暂只支持按时间点截单张图。 

        :param sync: The sync of this CreateThumbReq.
        :type: int
        """
        self._sync = sync

    @property
    def original_dir(self):
        """Gets the original_dir of this CreateThumbReq.

        是否使用原始输出目录。  取值如下： - 0：不使用原始输出目录，下发的输出目录后面追加随机目录，防止截图文件outputUri相同被覆盖。 - 1：使用原始输出目录。 

        :return: The original_dir of this CreateThumbReq.
        :rtype: int
        """
        return self._original_dir

    @original_dir.setter
    def original_dir(self, original_dir):
        """Sets the original_dir of this CreateThumbReq.

        是否使用原始输出目录。  取值如下： - 0：不使用原始输出目录，下发的输出目录后面追加随机目录，防止截图文件outputUri相同被覆盖。 - 1：使用原始输出目录。 

        :param original_dir: The original_dir of this CreateThumbReq.
        :type: int
        """
        self._original_dir = original_dir

    @property
    def project_id(self):
        """Gets the project_id of this CreateThumbReq.

        租户Id

        :return: The project_id of this CreateThumbReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateThumbReq.

        租户Id

        :param project_id: The project_id of this CreateThumbReq.
        :type: str
        """
        self._project_id = project_id

    @property
    def tenant_project_id(self):
        """Gets the tenant_project_id of this CreateThumbReq.

        vod租户Id

        :return: The tenant_project_id of this CreateThumbReq.
        :rtype: str
        """
        return self._tenant_project_id

    @tenant_project_id.setter
    def tenant_project_id(self, tenant_project_id):
        """Sets the tenant_project_id of this CreateThumbReq.

        vod租户Id

        :param tenant_project_id: The tenant_project_id of this CreateThumbReq.
        :type: str
        """
        self._tenant_project_id = tenant_project_id

    @property
    def domain_name(self):
        """Gets the domain_name of this CreateThumbReq.

        domain名称

        :return: The domain_name of this CreateThumbReq.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CreateThumbReq.

        domain名称

        :param domain_name: The domain_name of this CreateThumbReq.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def canonical_grant_id(self):
        """Gets the canonical_grant_id of this CreateThumbReq.

        用户domainId

        :return: The canonical_grant_id of this CreateThumbReq.
        :rtype: str
        """
        return self._canonical_grant_id

    @canonical_grant_id.setter
    def canonical_grant_id(self, canonical_grant_id):
        """Sets the canonical_grant_id of this CreateThumbReq.

        用户domainId

        :param canonical_grant_id: The canonical_grant_id of this CreateThumbReq.
        :type: str
        """
        self._canonical_grant_id = canonical_grant_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateThumbReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
