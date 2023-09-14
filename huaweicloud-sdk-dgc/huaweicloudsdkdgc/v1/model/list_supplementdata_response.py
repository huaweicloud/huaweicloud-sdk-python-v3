# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupplementdataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'msg': 'str',
        'rows': 'list[SupplementDataResp]',
        'success': 'bool',
        'total': 'int'
    }

    attribute_map = {
        'msg': 'msg',
        'rows': 'rows',
        'success': 'success',
        'total': 'total'
    }

    def __init__(self, msg=None, rows=None, success=None, total=None):
        """ListSupplementdataResponse

        The model defined in huaweicloud sdk

        :param msg: 
        :type msg: str
        :param rows: 包含若干补数据实例信息
        :type rows: list[:class:`huaweicloudsdkdgc.v1.SupplementDataResp`]
        :param success: 查询是否成功，取值为true或者false
        :type success: bool
        :param total: 补数据实例数量
        :type total: int
        """
        
        super(ListSupplementdataResponse, self).__init__()

        self._msg = None
        self._rows = None
        self._success = None
        self._total = None
        self.discriminator = None

        if msg is not None:
            self.msg = msg
        if rows is not None:
            self.rows = rows
        if success is not None:
            self.success = success
        if total is not None:
            self.total = total

    @property
    def msg(self):
        """Gets the msg of this ListSupplementdataResponse.

        :return: The msg of this ListSupplementdataResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this ListSupplementdataResponse.

        :param msg: The msg of this ListSupplementdataResponse.
        :type msg: str
        """
        self._msg = msg

    @property
    def rows(self):
        """Gets the rows of this ListSupplementdataResponse.

        包含若干补数据实例信息

        :return: The rows of this ListSupplementdataResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.SupplementDataResp`]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this ListSupplementdataResponse.

        包含若干补数据实例信息

        :param rows: The rows of this ListSupplementdataResponse.
        :type rows: list[:class:`huaweicloudsdkdgc.v1.SupplementDataResp`]
        """
        self._rows = rows

    @property
    def success(self):
        """Gets the success of this ListSupplementdataResponse.

        查询是否成功，取值为true或者false

        :return: The success of this ListSupplementdataResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ListSupplementdataResponse.

        查询是否成功，取值为true或者false

        :param success: The success of this ListSupplementdataResponse.
        :type success: bool
        """
        self._success = success

    @property
    def total(self):
        """Gets the total of this ListSupplementdataResponse.

        补数据实例数量

        :return: The total of this ListSupplementdataResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListSupplementdataResponse.

        补数据实例数量

        :param total: The total of this ListSupplementdataResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListSupplementdataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
