# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDeviceGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_id': 'int',
        'name': 'str',
        'description': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'parent_id': 'parent_id',
        'name': 'name',
        'description': 'description',
        'app_id': 'app_id'
    }

    def __init__(self, parent_id=None, name=None, description=None, app_id=None):
        """CreateDeviceGroupRequestBody

        The model defined in huaweicloud sdk

        :param parent_id: 父分组ID，自动向下取整
        :type parent_id: int
        :param name: 分组名称，支持中文，英文大小写，数字，下划线和中划线,长度2-64
        :type name: str
        :param description: 分组描述
        :type description: str
        :param app_id: 分组归属应用ID
        :type app_id: str
        """
        
        

        self._parent_id = None
        self._name = None
        self._description = None
        self._app_id = None
        self.discriminator = None

        self.parent_id = parent_id
        self.name = name
        if description is not None:
            self.description = description
        self.app_id = app_id

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateDeviceGroupRequestBody.

        父分组ID，自动向下取整

        :return: The parent_id of this CreateDeviceGroupRequestBody.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateDeviceGroupRequestBody.

        父分组ID，自动向下取整

        :param parent_id: The parent_id of this CreateDeviceGroupRequestBody.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this CreateDeviceGroupRequestBody.

        分组名称，支持中文，英文大小写，数字，下划线和中划线,长度2-64

        :return: The name of this CreateDeviceGroupRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDeviceGroupRequestBody.

        分组名称，支持中文，英文大小写，数字，下划线和中划线,长度2-64

        :param name: The name of this CreateDeviceGroupRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateDeviceGroupRequestBody.

        分组描述

        :return: The description of this CreateDeviceGroupRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDeviceGroupRequestBody.

        分组描述

        :param description: The description of this CreateDeviceGroupRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def app_id(self):
        """Gets the app_id of this CreateDeviceGroupRequestBody.

        分组归属应用ID

        :return: The app_id of this CreateDeviceGroupRequestBody.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateDeviceGroupRequestBody.

        分组归属应用ID

        :param app_id: The app_id of this CreateDeviceGroupRequestBody.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, CreateDeviceGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
