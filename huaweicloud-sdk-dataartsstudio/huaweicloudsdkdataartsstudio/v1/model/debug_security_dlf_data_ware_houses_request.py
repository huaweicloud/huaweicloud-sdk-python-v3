# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugSecurityDlfDataWareHousesRequest:

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
        'dw_id': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dw_id': 'dw_id'
    }

    def __init__(self, workspace=None, dw_id=None):
        """DebugSecurityDlfDataWareHousesRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param dw_id: 数据连接id
        :type dw_id: str
        """
        
        

        self._workspace = None
        self._dw_id = None
        self.discriminator = None

        self.workspace = workspace
        self.dw_id = dw_id

    @property
    def workspace(self):
        """Gets the workspace of this DebugSecurityDlfDataWareHousesRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this DebugSecurityDlfDataWareHousesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this DebugSecurityDlfDataWareHousesRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this DebugSecurityDlfDataWareHousesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dw_id(self):
        """Gets the dw_id of this DebugSecurityDlfDataWareHousesRequest.

        数据连接id

        :return: The dw_id of this DebugSecurityDlfDataWareHousesRequest.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        """Sets the dw_id of this DebugSecurityDlfDataWareHousesRequest.

        数据连接id

        :param dw_id: The dw_id of this DebugSecurityDlfDataWareHousesRequest.
        :type dw_id: str
        """
        self._dw_id = dw_id

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
        if not isinstance(other, DebugSecurityDlfDataWareHousesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
