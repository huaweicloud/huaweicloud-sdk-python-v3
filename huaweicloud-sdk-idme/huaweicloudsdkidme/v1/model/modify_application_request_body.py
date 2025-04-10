# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyApplicationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'description': 'str',
        'description_en': 'str',
        'permission_control': 'str',
        'app_user_list': 'list[AppUserList]'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'description_en': 'description_en',
        'permission_control': 'permission_control',
        'app_user_list': 'app_user_list'
    }

    def __init__(self, id=None, description=None, description_en=None, permission_control=None, app_user_list=None):
        r"""ModifyApplicationRequestBody

        The model defined in huaweicloud sdk

        :param id: 应用ID。
        :type id: str
        :param description: 应用的中文描述。
        :type description: str
        :param description_en: 应用的英文描述。
        :type description_en: str
        :param permission_control: app权限控制。 - NONE：关闭权限校验 - ALL：开启所有校验
        :type permission_control: str
        :param app_user_list: 应用责任人。
        :type app_user_list: list[:class:`huaweicloudsdkidme.v1.AppUserList`]
        """
        
        

        self._id = None
        self._description = None
        self._description_en = None
        self._permission_control = None
        self._app_user_list = None
        self.discriminator = None

        self.id = id
        self.description = description
        self.description_en = description_en
        if permission_control is not None:
            self.permission_control = permission_control
        self.app_user_list = app_user_list

    @property
    def id(self):
        r"""Gets the id of this ModifyApplicationRequestBody.

        应用ID。

        :return: The id of this ModifyApplicationRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModifyApplicationRequestBody.

        应用ID。

        :param id: The id of this ModifyApplicationRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this ModifyApplicationRequestBody.

        应用的中文描述。

        :return: The description of this ModifyApplicationRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModifyApplicationRequestBody.

        应用的中文描述。

        :param description: The description of this ModifyApplicationRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def description_en(self):
        r"""Gets the description_en of this ModifyApplicationRequestBody.

        应用的英文描述。

        :return: The description_en of this ModifyApplicationRequestBody.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        r"""Sets the description_en of this ModifyApplicationRequestBody.

        应用的英文描述。

        :param description_en: The description_en of this ModifyApplicationRequestBody.
        :type description_en: str
        """
        self._description_en = description_en

    @property
    def permission_control(self):
        r"""Gets the permission_control of this ModifyApplicationRequestBody.

        app权限控制。 - NONE：关闭权限校验 - ALL：开启所有校验

        :return: The permission_control of this ModifyApplicationRequestBody.
        :rtype: str
        """
        return self._permission_control

    @permission_control.setter
    def permission_control(self, permission_control):
        r"""Sets the permission_control of this ModifyApplicationRequestBody.

        app权限控制。 - NONE：关闭权限校验 - ALL：开启所有校验

        :param permission_control: The permission_control of this ModifyApplicationRequestBody.
        :type permission_control: str
        """
        self._permission_control = permission_control

    @property
    def app_user_list(self):
        r"""Gets the app_user_list of this ModifyApplicationRequestBody.

        应用责任人。

        :return: The app_user_list of this ModifyApplicationRequestBody.
        :rtype: list[:class:`huaweicloudsdkidme.v1.AppUserList`]
        """
        return self._app_user_list

    @app_user_list.setter
    def app_user_list(self, app_user_list):
        r"""Sets the app_user_list of this ModifyApplicationRequestBody.

        应用责任人。

        :param app_user_list: The app_user_list of this ModifyApplicationRequestBody.
        :type app_user_list: list[:class:`huaweicloudsdkidme.v1.AppUserList`]
        """
        self._app_user_list = app_user_list

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
        if not isinstance(other, ModifyApplicationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
