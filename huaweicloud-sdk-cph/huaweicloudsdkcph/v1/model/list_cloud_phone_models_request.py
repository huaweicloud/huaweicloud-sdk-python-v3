# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudPhoneModelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'status': 'status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, status=None, offset=None, limit=None):
        """ListCloudPhoneModelsRequest

        The model defined in huaweicloud sdk

        :param status: 规格状态 - 0：下线状态 - 1：正常使用 不传该参数表示查询所有状态的规格。
        :type status: int
        :param offset: 偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。
        :type offset: int
        :param limit: 每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。
        :type limit: int
        """
        
        

        self._status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def status(self):
        """Gets the status of this ListCloudPhoneModelsRequest.

        规格状态 - 0：下线状态 - 1：正常使用 不传该参数表示查询所有状态的规格。

        :return: The status of this ListCloudPhoneModelsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListCloudPhoneModelsRequest.

        规格状态 - 0：下线状态 - 1：正常使用 不传该参数表示查询所有状态的规格。

        :param status: The status of this ListCloudPhoneModelsRequest.
        :type status: int
        """
        self._status = status

    @property
    def offset(self):
        """Gets the offset of this ListCloudPhoneModelsRequest.

        偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :return: The offset of this ListCloudPhoneModelsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCloudPhoneModelsRequest.

        偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :param offset: The offset of this ListCloudPhoneModelsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCloudPhoneModelsRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :return: The limit of this ListCloudPhoneModelsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCloudPhoneModelsRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :param limit: The limit of this ListCloudPhoneModelsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListCloudPhoneModelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
