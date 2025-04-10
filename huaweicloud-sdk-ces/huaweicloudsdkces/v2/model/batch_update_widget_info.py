# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateWidgetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'widget_id': 'str',
        'ret_status': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'widget_id': 'widget_id',
        'ret_status': 'ret_status',
        'error_msg': 'error_msg'
    }

    def __init__(self, widget_id=None, ret_status=None, error_msg=None):
        r"""BatchUpdateWidgetInfo

        The model defined in huaweicloud sdk

        :param widget_id: 视图id
        :type widget_id: str
        :param ret_status: 修改结果；成功: successful, 失败: error 
        :type ret_status: str
        :param error_msg: 如果失败则返回失败信息
        :type error_msg: str
        """
        
        

        self._widget_id = None
        self._ret_status = None
        self._error_msg = None
        self.discriminator = None

        if widget_id is not None:
            self.widget_id = widget_id
        if ret_status is not None:
            self.ret_status = ret_status
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def widget_id(self):
        r"""Gets the widget_id of this BatchUpdateWidgetInfo.

        视图id

        :return: The widget_id of this BatchUpdateWidgetInfo.
        :rtype: str
        """
        return self._widget_id

    @widget_id.setter
    def widget_id(self, widget_id):
        r"""Sets the widget_id of this BatchUpdateWidgetInfo.

        视图id

        :param widget_id: The widget_id of this BatchUpdateWidgetInfo.
        :type widget_id: str
        """
        self._widget_id = widget_id

    @property
    def ret_status(self):
        r"""Gets the ret_status of this BatchUpdateWidgetInfo.

        修改结果；成功: successful, 失败: error 

        :return: The ret_status of this BatchUpdateWidgetInfo.
        :rtype: str
        """
        return self._ret_status

    @ret_status.setter
    def ret_status(self, ret_status):
        r"""Sets the ret_status of this BatchUpdateWidgetInfo.

        修改结果；成功: successful, 失败: error 

        :param ret_status: The ret_status of this BatchUpdateWidgetInfo.
        :type ret_status: str
        """
        self._ret_status = ret_status

    @property
    def error_msg(self):
        r"""Gets the error_msg of this BatchUpdateWidgetInfo.

        如果失败则返回失败信息

        :return: The error_msg of this BatchUpdateWidgetInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this BatchUpdateWidgetInfo.

        如果失败则返回失败信息

        :param error_msg: The error_msg of this BatchUpdateWidgetInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, BatchUpdateWidgetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
