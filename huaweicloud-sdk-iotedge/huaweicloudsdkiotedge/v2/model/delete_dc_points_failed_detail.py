# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDcPointsFailedDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'point_id': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'point_id': 'point_id'
    }

    def __init__(self, error_code=None, error_msg=None, point_id=None):
        r"""DeleteDcPointsFailedDetail

        The model defined in huaweicloud sdk

        :param error_code: 点位删除失败错误码
        :type error_code: str
        :param error_msg: 点位删除失败错误详情
        :type error_msg: str
        :param point_id: 点位id
        :type point_id: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self._point_id = None
        self.discriminator = None

        self.error_code = error_code
        self.error_msg = error_msg
        self.point_id = point_id

    @property
    def error_code(self):
        r"""Gets the error_code of this DeleteDcPointsFailedDetail.

        点位删除失败错误码

        :return: The error_code of this DeleteDcPointsFailedDetail.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this DeleteDcPointsFailedDetail.

        点位删除失败错误码

        :param error_code: The error_code of this DeleteDcPointsFailedDetail.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this DeleteDcPointsFailedDetail.

        点位删除失败错误详情

        :return: The error_msg of this DeleteDcPointsFailedDetail.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this DeleteDcPointsFailedDetail.

        点位删除失败错误详情

        :param error_msg: The error_msg of this DeleteDcPointsFailedDetail.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def point_id(self):
        r"""Gets the point_id of this DeleteDcPointsFailedDetail.

        点位id

        :return: The point_id of this DeleteDcPointsFailedDetail.
        :rtype: str
        """
        return self._point_id

    @point_id.setter
    def point_id(self, point_id):
        r"""Sets the point_id of this DeleteDcPointsFailedDetail.

        点位id

        :param point_id: The point_id of this DeleteDcPointsFailedDetail.
        :type point_id: str
        """
        self._point_id = point_id

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
        if not isinstance(other, DeleteDcPointsFailedDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
