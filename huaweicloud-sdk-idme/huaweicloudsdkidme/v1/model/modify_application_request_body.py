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
        'app_user_list': 'list[AppUserList]'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'description_en': 'description_en',
        'app_user_list': 'app_user_list'
    }

    def __init__(self, id=None, description=None, description_en=None, app_user_list=None):
        """ModifyApplicationRequestBody

        The model defined in huaweicloud sdk

        :param id: 应用ID。
        :type id: str
        :param description: 应用的中文描述。
        :type description: str
        :param description_en: 应用的英文描述。
        :type description_en: str
        :param app_user_list: 应用责任人。
        :type app_user_list: list[:class:`huaweicloudsdkidme.v1.AppUserList`]
        """
        
        

        self._id = None
        self._description = None
        self._description_en = None
        self._app_user_list = None
        self.discriminator = None

        self.id = id
        self.description = description
        self.description_en = description_en
        self.app_user_list = app_user_list

    @property
    def id(self):
        """Gets the id of this ModifyApplicationRequestBody.

        应用ID。

        :return: The id of this ModifyApplicationRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModifyApplicationRequestBody.

        应用ID。

        :param id: The id of this ModifyApplicationRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this ModifyApplicationRequestBody.

        应用的中文描述。

        :return: The description of this ModifyApplicationRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyApplicationRequestBody.

        应用的中文描述。

        :param description: The description of this ModifyApplicationRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def description_en(self):
        """Gets the description_en of this ModifyApplicationRequestBody.

        应用的英文描述。

        :return: The description_en of this ModifyApplicationRequestBody.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        """Sets the description_en of this ModifyApplicationRequestBody.

        应用的英文描述。

        :param description_en: The description_en of this ModifyApplicationRequestBody.
        :type description_en: str
        """
        self._description_en = description_en

    @property
    def app_user_list(self):
        """Gets the app_user_list of this ModifyApplicationRequestBody.

        应用责任人。

        :return: The app_user_list of this ModifyApplicationRequestBody.
        :rtype: list[:class:`huaweicloudsdkidme.v1.AppUserList`]
        """
        return self._app_user_list

    @app_user_list.setter
    def app_user_list(self, app_user_list):
        """Sets the app_user_list of this ModifyApplicationRequestBody.

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
