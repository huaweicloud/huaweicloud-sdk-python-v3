# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPtrRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'offset': 'int',
        'enterprise_project_id': 'str',
        'tags': 'str',
        'status': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'offset': 'offset',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'status': 'status'
    }

    def __init__(self, marker=None, limit=None, offset=None, enterprise_project_id=None, tags=None, status=None):
        r"""ListPtrRecordsRequest

        The model defined in huaweicloud sdk

        :param marker: 分页查询起始的资源ID，为空时为查询第一页。  默认值为空。
        :type marker: str
        :param limit: 分页查询时配置每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。
        :type limit: int
        :param offset: 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当设置marker不为空时，以marker为分页起始标识，offset不生效。
        :type offset: int
        :param enterprise_project_id: 反向解析关联的企业项目ID，长度不超过36个字符。
        :type enterprise_project_id: str
        :param tags: 资源标签。  取值格式：key1,value1|key2,value2  多个标签之间用“|”分开，每个标签的键值用英文逗号“,”相隔。
        :type tags: str
        :param status: 资源状态。
        :type status: str
        """
        
        

        self._marker = None
        self._limit = None
        self._offset = None
        self._enterprise_project_id = None
        self._tags = None
        self._status = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status

    @property
    def marker(self):
        r"""Gets the marker of this ListPtrRecordsRequest.

        分页查询起始的资源ID，为空时为查询第一页。  默认值为空。

        :return: The marker of this ListPtrRecordsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPtrRecordsRequest.

        分页查询起始的资源ID，为空时为查询第一页。  默认值为空。

        :param marker: The marker of this ListPtrRecordsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListPtrRecordsRequest.

        分页查询时配置每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。

        :return: The limit of this ListPtrRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPtrRecordsRequest.

        分页查询时配置每页返回的资源个数。  取值范围：0~500  取值一般为10，20，50。默认值为500。

        :param limit: The limit of this ListPtrRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPtrRecordsRequest.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当设置marker不为空时，以marker为分页起始标识，offset不生效。

        :return: The offset of this ListPtrRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPtrRecordsRequest.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。  取值范围：0~2147483647  默认值为0。  当设置marker不为空时，以marker为分页起始标识，offset不生效。

        :param offset: The offset of this ListPtrRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPtrRecordsRequest.

        反向解析关联的企业项目ID，长度不超过36个字符。

        :return: The enterprise_project_id of this ListPtrRecordsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPtrRecordsRequest.

        反向解析关联的企业项目ID，长度不超过36个字符。

        :param enterprise_project_id: The enterprise_project_id of this ListPtrRecordsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this ListPtrRecordsRequest.

        资源标签。  取值格式：key1,value1|key2,value2  多个标签之间用“|”分开，每个标签的键值用英文逗号“,”相隔。

        :return: The tags of this ListPtrRecordsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListPtrRecordsRequest.

        资源标签。  取值格式：key1,value1|key2,value2  多个标签之间用“|”分开，每个标签的键值用英文逗号“,”相隔。

        :param tags: The tags of this ListPtrRecordsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def status(self):
        r"""Gets the status of this ListPtrRecordsRequest.

        资源状态。

        :return: The status of this ListPtrRecordsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPtrRecordsRequest.

        资源状态。

        :param status: The status of this ListPtrRecordsRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListPtrRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
