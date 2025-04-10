# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLineageRequest:

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
        'guid': 'str',
        'direction': 'str',
        'depth': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'guid': 'guid',
        'direction': 'direction',
        'depth': 'depth'
    }

    def __init__(self, workspace=None, guid=None, direction=None, depth=None):
        r"""ShowLineageRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param guid: 资产guid
        :type guid: str
        :param direction: 查询方向，取值范围：BOTH、IN、OUT。默认BOTH
        :type direction: str
        :param depth: 血缘链路长度，默认值5
        :type depth: int
        """
        
        

        self._workspace = None
        self._guid = None
        self._direction = None
        self._depth = None
        self.discriminator = None

        self.workspace = workspace
        self.guid = guid
        if direction is not None:
            self.direction = direction
        if depth is not None:
            self.depth = depth

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowLineageRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ShowLineageRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowLineageRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ShowLineageRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def guid(self):
        r"""Gets the guid of this ShowLineageRequest.

        资产guid

        :return: The guid of this ShowLineageRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this ShowLineageRequest.

        资产guid

        :param guid: The guid of this ShowLineageRequest.
        :type guid: str
        """
        self._guid = guid

    @property
    def direction(self):
        r"""Gets the direction of this ShowLineageRequest.

        查询方向，取值范围：BOTH、IN、OUT。默认BOTH

        :return: The direction of this ShowLineageRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this ShowLineageRequest.

        查询方向，取值范围：BOTH、IN、OUT。默认BOTH

        :param direction: The direction of this ShowLineageRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def depth(self):
        r"""Gets the depth of this ShowLineageRequest.

        血缘链路长度，默认值5

        :return: The depth of this ShowLineageRequest.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        r"""Sets the depth of this ShowLineageRequest.

        血缘链路长度，默认值5

        :param depth: The depth of this ShowLineageRequest.
        :type depth: int
        """
        self._depth = depth

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
        if not isinstance(other, ShowLineageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
