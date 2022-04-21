# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryNaBriefResponseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'na_id': 'str',
        'name': 'str',
        'description': 'str',
        'endpoint': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'na_id': 'na_id',
        'name': 'name',
        'description': 'description',
        'endpoint': 'endpoint',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, na_id=None, name=None, description=None, endpoint=None, create_time=None, update_time=None):
        """QueryNaBriefResponseDTO

        The model defined in huaweicloud sdk

        :param na_id: NA系统ID，提供给其他系统访问的唯一标识
        :type na_id: str
        :param name: NA系统名称
        :type name: str
        :param description: 北向NA系统描述
        :type description: str
        :param endpoint: 访问URL地址
        :type endpoint: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._na_id = None
        self._name = None
        self._description = None
        self._endpoint = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if na_id is not None:
            self.na_id = na_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if endpoint is not None:
            self.endpoint = endpoint
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def na_id(self):
        """Gets the na_id of this QueryNaBriefResponseDTO.

        NA系统ID，提供给其他系统访问的唯一标识

        :return: The na_id of this QueryNaBriefResponseDTO.
        :rtype: str
        """
        return self._na_id

    @na_id.setter
    def na_id(self, na_id):
        """Sets the na_id of this QueryNaBriefResponseDTO.

        NA系统ID，提供给其他系统访问的唯一标识

        :param na_id: The na_id of this QueryNaBriefResponseDTO.
        :type na_id: str
        """
        self._na_id = na_id

    @property
    def name(self):
        """Gets the name of this QueryNaBriefResponseDTO.

        NA系统名称

        :return: The name of this QueryNaBriefResponseDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryNaBriefResponseDTO.

        NA系统名称

        :param name: The name of this QueryNaBriefResponseDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this QueryNaBriefResponseDTO.

        北向NA系统描述

        :return: The description of this QueryNaBriefResponseDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryNaBriefResponseDTO.

        北向NA系统描述

        :param description: The description of this QueryNaBriefResponseDTO.
        :type description: str
        """
        self._description = description

    @property
    def endpoint(self):
        """Gets the endpoint of this QueryNaBriefResponseDTO.

        访问URL地址

        :return: The endpoint of this QueryNaBriefResponseDTO.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this QueryNaBriefResponseDTO.

        访问URL地址

        :param endpoint: The endpoint of this QueryNaBriefResponseDTO.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def create_time(self):
        """Gets the create_time of this QueryNaBriefResponseDTO.

        创建时间

        :return: The create_time of this QueryNaBriefResponseDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryNaBriefResponseDTO.

        创建时间

        :param create_time: The create_time of this QueryNaBriefResponseDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this QueryNaBriefResponseDTO.

        更新时间

        :return: The update_time of this QueryNaBriefResponseDTO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this QueryNaBriefResponseDTO.

        更新时间

        :param update_time: The update_time of this QueryNaBriefResponseDTO.
        :type update_time: str
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
        if not isinstance(other, QueryNaBriefResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
