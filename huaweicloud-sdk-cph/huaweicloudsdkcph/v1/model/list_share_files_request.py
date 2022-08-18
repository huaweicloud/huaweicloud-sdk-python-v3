# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShareFilesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'server_ids': 'str',
        'path': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'server_ids': 'server_ids',
        'path': 'path'
    }

    def __init__(self, offset=None, limit=None, server_ids=None, path=None):
        """ListShareFilesRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。
        :type offset: int
        :param limit: 每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。
        :type limit: int
        :param server_ids: 云手机服务器ID列表，多个服务器ID用逗号（,）分隔。
        :type server_ids: str
        :param path: 待查询的目录名称 可以包含大小写字母、数字、“.”、“+”、“-”、“_”、“/”、\&quot;&#x3D;\&quot;；必须以“/”开头，并且不能只包含“/”；不能包含“../”、“//”等。 示例：/data/data
        :type path: str
        """
        
        

        self._offset = None
        self._limit = None
        self._server_ids = None
        self._path = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.server_ids = server_ids
        self.path = path

    @property
    def offset(self):
        """Gets the offset of this ListShareFilesRequest.

        偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :return: The offset of this ListShareFilesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListShareFilesRequest.

        偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :param offset: The offset of this ListShareFilesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListShareFilesRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :return: The limit of this ListShareFilesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListShareFilesRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :param limit: The limit of this ListShareFilesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def server_ids(self):
        """Gets the server_ids of this ListShareFilesRequest.

        云手机服务器ID列表，多个服务器ID用逗号（,）分隔。

        :return: The server_ids of this ListShareFilesRequest.
        :rtype: str
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        """Sets the server_ids of this ListShareFilesRequest.

        云手机服务器ID列表，多个服务器ID用逗号（,）分隔。

        :param server_ids: The server_ids of this ListShareFilesRequest.
        :type server_ids: str
        """
        self._server_ids = server_ids

    @property
    def path(self):
        """Gets the path of this ListShareFilesRequest.

        待查询的目录名称 可以包含大小写字母、数字、“.”、“+”、“-”、“_”、“/”、\"=\"；必须以“/”开头，并且不能只包含“/”；不能包含“../”、“//”等。 示例：/data/data

        :return: The path of this ListShareFilesRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ListShareFilesRequest.

        待查询的目录名称 可以包含大小写字母、数字、“.”、“+”、“-”、“_”、“/”、\"=\"；必须以“/”开头，并且不能只包含“/”；不能包含“../”、“//”等。 示例：/data/data

        :param path: The path of this ListShareFilesRequest.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, ListShareFilesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
