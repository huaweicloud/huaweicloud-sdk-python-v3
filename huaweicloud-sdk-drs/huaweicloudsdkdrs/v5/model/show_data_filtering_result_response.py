# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataFilteringResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_count': 'int',
        'failed_count': 'int',
        'db_object_filtering_result': 'list[DbObjectFilteringResult]'
    }

    attribute_map = {
        'success_count': 'success_count',
        'failed_count': 'failed_count',
        'db_object_filtering_result': 'db_object_filtering_result'
    }

    def __init__(self, success_count=None, failed_count=None, db_object_filtering_result=None):
        r"""ShowDataFilteringResultResponse

        The model defined in huaweicloud sdk

        :param success_count: 数据过滤规则校验成功的数量
        :type success_count: int
        :param failed_count: 数据过滤规则校验失败的数量
        :type failed_count: int
        :param db_object_filtering_result: 库表过滤规则校验结果
        :type db_object_filtering_result: list[:class:`huaweicloudsdkdrs.v5.DbObjectFilteringResult`]
        """
        
        super(ShowDataFilteringResultResponse, self).__init__()

        self._success_count = None
        self._failed_count = None
        self._db_object_filtering_result = None
        self.discriminator = None

        if success_count is not None:
            self.success_count = success_count
        if failed_count is not None:
            self.failed_count = failed_count
        if db_object_filtering_result is not None:
            self.db_object_filtering_result = db_object_filtering_result

    @property
    def success_count(self):
        r"""Gets the success_count of this ShowDataFilteringResultResponse.

        数据过滤规则校验成功的数量

        :return: The success_count of this ShowDataFilteringResultResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this ShowDataFilteringResultResponse.

        数据过滤规则校验成功的数量

        :param success_count: The success_count of this ShowDataFilteringResultResponse.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def failed_count(self):
        r"""Gets the failed_count of this ShowDataFilteringResultResponse.

        数据过滤规则校验失败的数量

        :return: The failed_count of this ShowDataFilteringResultResponse.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        r"""Sets the failed_count of this ShowDataFilteringResultResponse.

        数据过滤规则校验失败的数量

        :param failed_count: The failed_count of this ShowDataFilteringResultResponse.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def db_object_filtering_result(self):
        r"""Gets the db_object_filtering_result of this ShowDataFilteringResultResponse.

        库表过滤规则校验结果

        :return: The db_object_filtering_result of this ShowDataFilteringResultResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DbObjectFilteringResult`]
        """
        return self._db_object_filtering_result

    @db_object_filtering_result.setter
    def db_object_filtering_result(self, db_object_filtering_result):
        r"""Sets the db_object_filtering_result of this ShowDataFilteringResultResponse.

        库表过滤规则校验结果

        :param db_object_filtering_result: The db_object_filtering_result of this ShowDataFilteringResultResponse.
        :type db_object_filtering_result: list[:class:`huaweicloudsdkdrs.v5.DbObjectFilteringResult`]
        """
        self._db_object_filtering_result = db_object_filtering_result

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
        if not isinstance(other, ShowDataFilteringResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
