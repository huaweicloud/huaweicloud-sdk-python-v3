# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDataspaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'dataspace_id': 'str',
        'dataspace_name': 'str',
        'dataspace_type': 'str',
        'description': 'str',
        'create_by': 'str',
        'create_time': 'int',
        'update_by': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'dataspace_id': 'dataspace_id',
        'dataspace_name': 'dataspace_name',
        'dataspace_type': 'dataspace_type',
        'description': 'description',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'update_by': 'update_by',
        'update_time': 'update_time'
    }

    def __init__(self, domain_id=None, region_id=None, project_id=None, dataspace_id=None, dataspace_name=None, dataspace_type=None, description=None, create_by=None, create_time=None, update_by=None, update_time=None):
        r"""CreateDataspaceResponse

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param region_id: region ID
        :type region_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param dataspace_id: 工作空间ID
        :type dataspace_id: str
        :param dataspace_name: 工作空间名称
        :type dataspace_name: str
        :param dataspace_type: 数据空间类型；可选值：system-defined(系统预定义)、user-defined(用户自定义)
        :type dataspace_type: str
        :param description: 描述
        :type description: str
        :param create_by: 创建者
        :type create_by: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_by: 更新者
        :type update_by: str
        :param update_time: 更新时间
        :type update_time: int
        """
        
        super(CreateDataspaceResponse, self).__init__()

        self._domain_id = None
        self._region_id = None
        self._project_id = None
        self._dataspace_id = None
        self._dataspace_name = None
        self._dataspace_type = None
        self._description = None
        self._create_by = None
        self._create_time = None
        self._update_by = None
        self._update_time = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if dataspace_id is not None:
            self.dataspace_id = dataspace_id
        if dataspace_name is not None:
            self.dataspace_name = dataspace_name
        if dataspace_type is not None:
            self.dataspace_type = dataspace_type
        if description is not None:
            self.description = description
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateDataspaceResponse.

        账号ID

        :return: The domain_id of this CreateDataspaceResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateDataspaceResponse.

        账号ID

        :param domain_id: The domain_id of this CreateDataspaceResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateDataspaceResponse.

        region ID

        :return: The region_id of this CreateDataspaceResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateDataspaceResponse.

        region ID

        :param region_id: The region_id of this CreateDataspaceResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateDataspaceResponse.

        项目ID

        :return: The project_id of this CreateDataspaceResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateDataspaceResponse.

        项目ID

        :param project_id: The project_id of this CreateDataspaceResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this CreateDataspaceResponse.

        工作空间ID

        :return: The dataspace_id of this CreateDataspaceResponse.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this CreateDataspaceResponse.

        工作空间ID

        :param dataspace_id: The dataspace_id of this CreateDataspaceResponse.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def dataspace_name(self):
        r"""Gets the dataspace_name of this CreateDataspaceResponse.

        工作空间名称

        :return: The dataspace_name of this CreateDataspaceResponse.
        :rtype: str
        """
        return self._dataspace_name

    @dataspace_name.setter
    def dataspace_name(self, dataspace_name):
        r"""Sets the dataspace_name of this CreateDataspaceResponse.

        工作空间名称

        :param dataspace_name: The dataspace_name of this CreateDataspaceResponse.
        :type dataspace_name: str
        """
        self._dataspace_name = dataspace_name

    @property
    def dataspace_type(self):
        r"""Gets the dataspace_type of this CreateDataspaceResponse.

        数据空间类型；可选值：system-defined(系统预定义)、user-defined(用户自定义)

        :return: The dataspace_type of this CreateDataspaceResponse.
        :rtype: str
        """
        return self._dataspace_type

    @dataspace_type.setter
    def dataspace_type(self, dataspace_type):
        r"""Sets the dataspace_type of this CreateDataspaceResponse.

        数据空间类型；可选值：system-defined(系统预定义)、user-defined(用户自定义)

        :param dataspace_type: The dataspace_type of this CreateDataspaceResponse.
        :type dataspace_type: str
        """
        self._dataspace_type = dataspace_type

    @property
    def description(self):
        r"""Gets the description of this CreateDataspaceResponse.

        描述

        :return: The description of this CreateDataspaceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDataspaceResponse.

        描述

        :param description: The description of this CreateDataspaceResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_by(self):
        r"""Gets the create_by of this CreateDataspaceResponse.

        创建者

        :return: The create_by of this CreateDataspaceResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this CreateDataspaceResponse.

        创建者

        :param create_by: The create_by of this CreateDataspaceResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateDataspaceResponse.

        创建时间

        :return: The create_time of this CreateDataspaceResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateDataspaceResponse.

        创建时间

        :param create_time: The create_time of this CreateDataspaceResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_by(self):
        r"""Gets the update_by of this CreateDataspaceResponse.

        更新者

        :return: The update_by of this CreateDataspaceResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this CreateDataspaceResponse.

        更新者

        :param update_by: The update_by of this CreateDataspaceResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateDataspaceResponse.

        更新时间

        :return: The update_time of this CreateDataspaceResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateDataspaceResponse.

        更新时间

        :param update_time: The update_time of this CreateDataspaceResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateDataspaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
