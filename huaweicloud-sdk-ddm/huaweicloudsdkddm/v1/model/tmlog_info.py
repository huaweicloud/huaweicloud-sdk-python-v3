# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TmlogInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'file_list': 'list[str]',
        'tmlog_size': 'float'
    }

    attribute_map = {
        'node_id': 'node_id',
        'file_list': 'file_list',
        'tmlog_size': 'tmlog_size'
    }

    def __init__(self, node_id=None, file_list=None, tmlog_size=None):
        r"""TmlogInfo

        The model defined in huaweicloud sdk

        :param node_id: 节点ID
        :type node_id: str
        :param file_list: 压缩文件列表
        :type file_list: list[str]
        :param tmlog_size: TMLOG文件大小单位（MB）。
        :type tmlog_size: float
        """
        
        

        self._node_id = None
        self._file_list = None
        self._tmlog_size = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if file_list is not None:
            self.file_list = file_list
        if tmlog_size is not None:
            self.tmlog_size = tmlog_size

    @property
    def node_id(self):
        r"""Gets the node_id of this TmlogInfo.

        节点ID

        :return: The node_id of this TmlogInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this TmlogInfo.

        节点ID

        :param node_id: The node_id of this TmlogInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def file_list(self):
        r"""Gets the file_list of this TmlogInfo.

        压缩文件列表

        :return: The file_list of this TmlogInfo.
        :rtype: list[str]
        """
        return self._file_list

    @file_list.setter
    def file_list(self, file_list):
        r"""Sets the file_list of this TmlogInfo.

        压缩文件列表

        :param file_list: The file_list of this TmlogInfo.
        :type file_list: list[str]
        """
        self._file_list = file_list

    @property
    def tmlog_size(self):
        r"""Gets the tmlog_size of this TmlogInfo.

        TMLOG文件大小单位（MB）。

        :return: The tmlog_size of this TmlogInfo.
        :rtype: float
        """
        return self._tmlog_size

    @tmlog_size.setter
    def tmlog_size(self, tmlog_size):
        r"""Sets the tmlog_size of this TmlogInfo.

        TMLOG文件大小单位（MB）。

        :param tmlog_size: The tmlog_size of this TmlogInfo.
        :type tmlog_size: float
        """
        self._tmlog_size = tmlog_size

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TmlogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
