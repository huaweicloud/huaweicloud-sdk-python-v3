# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFactorySupplementDataResponse(SdkResponse):

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
        'rows': 'list[SupplementDataRespRows]',
        'success': 'bool',
        'total': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'msg': 'msg',
        'rows': 'rows',
        'success': 'success',
        'total': 'total',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, msg=None, rows=None, success=None, total=None, x_request_id=None):
        r"""ShowFactorySupplementDataResponse

        The model defined in huaweicloud sdk

        :param msg: success
        :type msg: str
        :param rows: 包含若干补数据实例信息
        :type rows: list[:class:`huaweicloudsdkdataartsstudio.v1.SupplementDataRespRows`]
        :param success: 查询是否成功，取值为true或者false
        :type success: bool
        :param total: 补数据实例数量
        :type total: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowFactorySupplementDataResponse, self).__init__()

        self._msg = None
        self._rows = None
        self._success = None
        self._total = None
        self._x_request_id = None
        self.discriminator = None

        if msg is not None:
            self.msg = msg
        if rows is not None:
            self.rows = rows
        if success is not None:
            self.success = success
        if total is not None:
            self.total = total
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def msg(self):
        r"""Gets the msg of this ShowFactorySupplementDataResponse.

        success

        :return: The msg of this ShowFactorySupplementDataResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this ShowFactorySupplementDataResponse.

        success

        :param msg: The msg of this ShowFactorySupplementDataResponse.
        :type msg: str
        """
        self._msg = msg

    @property
    def rows(self):
        r"""Gets the rows of this ShowFactorySupplementDataResponse.

        包含若干补数据实例信息

        :return: The rows of this ShowFactorySupplementDataResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SupplementDataRespRows`]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        r"""Sets the rows of this ShowFactorySupplementDataResponse.

        包含若干补数据实例信息

        :param rows: The rows of this ShowFactorySupplementDataResponse.
        :type rows: list[:class:`huaweicloudsdkdataartsstudio.v1.SupplementDataRespRows`]
        """
        self._rows = rows

    @property
    def success(self):
        r"""Gets the success of this ShowFactorySupplementDataResponse.

        查询是否成功，取值为true或者false

        :return: The success of this ShowFactorySupplementDataResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ShowFactorySupplementDataResponse.

        查询是否成功，取值为true或者false

        :param success: The success of this ShowFactorySupplementDataResponse.
        :type success: bool
        """
        self._success = success

    @property
    def total(self):
        r"""Gets the total of this ShowFactorySupplementDataResponse.

        补数据实例数量

        :return: The total of this ShowFactorySupplementDataResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowFactorySupplementDataResponse.

        补数据实例数量

        :param total: The total of this ShowFactorySupplementDataResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowFactorySupplementDataResponse.

        :return: The x_request_id of this ShowFactorySupplementDataResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowFactorySupplementDataResponse.

        :param x_request_id: The x_request_id of this ShowFactorySupplementDataResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowFactorySupplementDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
