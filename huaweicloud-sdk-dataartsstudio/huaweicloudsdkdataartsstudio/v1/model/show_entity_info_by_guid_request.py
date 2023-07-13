# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEntityInfoByGuidRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'guid': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'guid': 'guid'
    }

    def __init__(self, workspace=None, guid=None):
        """ShowEntityInfoByGuidRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param guid: 资产的guid
        :type guid: str
        """
        
        

        self._workspace = None
        self._guid = None
        self.discriminator = None

        self.workspace = workspace
        self.guid = guid

    @property
    def workspace(self):
        """Gets the workspace of this ShowEntityInfoByGuidRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ShowEntityInfoByGuidRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowEntityInfoByGuidRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ShowEntityInfoByGuidRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def guid(self):
        """Gets the guid of this ShowEntityInfoByGuidRequest.

        资产的guid

        :return: The guid of this ShowEntityInfoByGuidRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this ShowEntityInfoByGuidRequest.

        资产的guid

        :param guid: The guid of this ShowEntityInfoByGuidRequest.
        :type guid: str
        """
        self._guid = guid

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
        if not isinstance(other, ShowEntityInfoByGuidRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
