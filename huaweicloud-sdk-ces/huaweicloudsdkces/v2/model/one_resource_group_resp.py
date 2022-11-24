# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OneResourceGroupResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'group_id': 'str',
        'create_time': 'datetime',
        'enterprise_project_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_id': 'group_id',
        'create_time': 'create_time',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type'
    }

    def __init__(self, group_name=None, group_id=None, create_time=None, enterprise_project_id=None, type=None):
        """OneResourceGroupResp

        The model defined in huaweicloud sdk

        :param group_name: 资源分组的名称
        :type group_name: str
        :param group_id: 资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串
        :type group_id: str
        :param create_time: 资源分组的创建时间
        :type create_time: datetime
        :param enterprise_project_id: 资源分组归属企业项目ID
        :type enterprise_project_id: str
        :param type: 资源分组创建方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,Manual（手动添加）
        :type type: str
        """
        
        

        self._group_name = None
        self._group_id = None
        self._create_time = None
        self._enterprise_project_id = None
        self._type = None
        self.discriminator = None

        self.group_name = group_name
        self.group_id = group_id
        self.create_time = create_time
        self.enterprise_project_id = enterprise_project_id
        self.type = type

    @property
    def group_name(self):
        """Gets the group_name of this OneResourceGroupResp.

        资源分组的名称

        :return: The group_name of this OneResourceGroupResp.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this OneResourceGroupResp.

        资源分组的名称

        :param group_name: The group_name of this OneResourceGroupResp.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        """Gets the group_id of this OneResourceGroupResp.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :return: The group_id of this OneResourceGroupResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this OneResourceGroupResp.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :param group_id: The group_id of this OneResourceGroupResp.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def create_time(self):
        """Gets the create_time of this OneResourceGroupResp.

        资源分组的创建时间

        :return: The create_time of this OneResourceGroupResp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this OneResourceGroupResp.

        资源分组的创建时间

        :param create_time: The create_time of this OneResourceGroupResp.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this OneResourceGroupResp.

        资源分组归属企业项目ID

        :return: The enterprise_project_id of this OneResourceGroupResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this OneResourceGroupResp.

        资源分组归属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this OneResourceGroupResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        """Gets the type of this OneResourceGroupResp.

        资源分组创建方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,Manual（手动添加）

        :return: The type of this OneResourceGroupResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneResourceGroupResp.

        资源分组创建方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,Manual（手动添加）

        :param type: The type of this OneResourceGroupResp.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, OneResourceGroupResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
