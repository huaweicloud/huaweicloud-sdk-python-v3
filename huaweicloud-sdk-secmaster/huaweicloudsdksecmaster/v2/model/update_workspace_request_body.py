# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkspaceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'view_bind_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'view_bind_id': 'view_bind_id'
    }

    def __init__(self, name=None, description=None, view_bind_id=None):
        r"""UpdateWorkspaceRequestBody

        The model defined in huaweicloud sdk

        :param name: 工作空间名称
        :type name: str
        :param description: 工作空间描述
        :type description: str
        :param view_bind_id: 视图绑定的空间id
        :type view_bind_id: str
        """
        
        

        self._name = None
        self._description = None
        self._view_bind_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if view_bind_id is not None:
            self.view_bind_id = view_bind_id

    @property
    def name(self):
        r"""Gets the name of this UpdateWorkspaceRequestBody.

        工作空间名称

        :return: The name of this UpdateWorkspaceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateWorkspaceRequestBody.

        工作空间名称

        :param name: The name of this UpdateWorkspaceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateWorkspaceRequestBody.

        工作空间描述

        :return: The description of this UpdateWorkspaceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateWorkspaceRequestBody.

        工作空间描述

        :param description: The description of this UpdateWorkspaceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def view_bind_id(self):
        r"""Gets the view_bind_id of this UpdateWorkspaceRequestBody.

        视图绑定的空间id

        :return: The view_bind_id of this UpdateWorkspaceRequestBody.
        :rtype: str
        """
        return self._view_bind_id

    @view_bind_id.setter
    def view_bind_id(self, view_bind_id):
        r"""Sets the view_bind_id of this UpdateWorkspaceRequestBody.

        视图绑定的空间id

        :param view_bind_id: The view_bind_id of this UpdateWorkspaceRequestBody.
        :type view_bind_id: str
        """
        self._view_bind_id = view_bind_id

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
        if not isinstance(other, UpdateWorkspaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
