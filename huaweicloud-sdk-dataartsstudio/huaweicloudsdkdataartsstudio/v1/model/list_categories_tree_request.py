# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCategoriesTreeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'instance': 'instance',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, instance=None, workspace_id=None):
        r"""ListCategoriesTreeRequest

        The model defined in huaweicloud sdk

        :param instance: 实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type instance: str
        :param workspace_id: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace_id: str
        """
        
        

        self._instance = None
        self._workspace_id = None
        self.discriminator = None

        self.instance = instance
        self.workspace_id = workspace_id

    @property
    def instance(self):
        r"""Gets the instance of this ListCategoriesTreeRequest.

        实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The instance of this ListCategoriesTreeRequest.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this ListCategoriesTreeRequest.

        实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param instance: The instance of this ListCategoriesTreeRequest.
        :type instance: str
        """
        self._instance = instance

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListCategoriesTreeRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace_id of this ListCategoriesTreeRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListCategoriesTreeRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace_id: The workspace_id of this ListCategoriesTreeRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, ListCategoriesTreeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
