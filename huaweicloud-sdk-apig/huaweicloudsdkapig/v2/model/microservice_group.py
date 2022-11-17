# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicroserviceGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'app_id': 'app_id'
    }

    def __init__(self, group_id=None, group_name=None, app_id=None):
        """MicroserviceGroup

        The model defined in huaweicloud sdk

        :param group_id: 指定已有的分组，为空时创建新的分组
        :type group_id: str
        :param group_name: API分组的名称,group_id为空时必填。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type group_name: str
        :param app_id: group_id为空时必填，指定新分组所属的集成应用
        :type app_id: str
        """
        
        

        self._group_id = None
        self._group_name = None
        self._app_id = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if app_id is not None:
            self.app_id = app_id

    @property
    def group_id(self):
        """Gets the group_id of this MicroserviceGroup.

        指定已有的分组，为空时创建新的分组

        :return: The group_id of this MicroserviceGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this MicroserviceGroup.

        指定已有的分组，为空时创建新的分组

        :param group_id: The group_id of this MicroserviceGroup.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this MicroserviceGroup.

        API分组的名称,group_id为空时必填。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The group_name of this MicroserviceGroup.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this MicroserviceGroup.

        API分组的名称,group_id为空时必填。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param group_name: The group_name of this MicroserviceGroup.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def app_id(self):
        """Gets the app_id of this MicroserviceGroup.

        group_id为空时必填，指定新分组所属的集成应用

        :return: The app_id of this MicroserviceGroup.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this MicroserviceGroup.

        group_id为空时必填，指定新分组所属的集成应用

        :param app_id: The app_id of this MicroserviceGroup.
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
        if not isinstance(other, MicroserviceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
