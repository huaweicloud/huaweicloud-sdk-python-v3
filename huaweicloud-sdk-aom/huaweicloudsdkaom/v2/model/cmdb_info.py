# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CmdbInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'node_ids': 'list[NodeInfo]'
    }

    attribute_map = {
        'app_id': 'app_id',
        'node_ids': 'node_ids'
    }

    def __init__(self, app_id=None, node_ids=None):
        r"""CmdbInfo

        The model defined in huaweicloud sdk

        :param app_id: 应用id。
        :type app_id: str
        :param node_ids: 节点信息列表。
        :type node_ids: list[:class:`huaweicloudsdkaom.v2.NodeInfo`]
        """
        
        

        self._app_id = None
        self._node_ids = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if node_ids is not None:
            self.node_ids = node_ids

    @property
    def app_id(self):
        r"""Gets the app_id of this CmdbInfo.

        应用id。

        :return: The app_id of this CmdbInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CmdbInfo.

        应用id。

        :param app_id: The app_id of this CmdbInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def node_ids(self):
        r"""Gets the node_ids of this CmdbInfo.

        节点信息列表。

        :return: The node_ids of this CmdbInfo.
        :rtype: list[:class:`huaweicloudsdkaom.v2.NodeInfo`]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this CmdbInfo.

        节点信息列表。

        :param node_ids: The node_ids of this CmdbInfo.
        :type node_ids: list[:class:`huaweicloudsdkaom.v2.NodeInfo`]
        """
        self._node_ids = node_ids

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
        if not isinstance(other, CmdbInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
