# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSendSmsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'int',
        'sms_content': 'str',
        'cids': 'list[str]',
        'order_id': 'int',
        'file_temp_id': 'int'
    }

    attribute_map = {
        'template_id': 'template_id',
        'sms_content': 'sms_content',
        'cids': 'cids',
        'order_id': 'order_id',
        'file_temp_id': 'file_temp_id'
    }

    def __init__(self, template_id=None, sms_content=None, cids=None, order_id=None, file_temp_id=None):
        """CreateSendSmsReq

        The model defined in huaweicloud sdk

        :param template_id: 模板id
        :type template_id: int
        :param sms_content: 短信内容
        :type sms_content: str
        :param cids: 容器ID
        :type cids: list[str]
        :param order_id: 批次号
        :type order_id: int
        :param file_temp_id: 临时文件ID
        :type file_temp_id: int
        """
        
        

        self._template_id = None
        self._sms_content = None
        self._cids = None
        self._order_id = None
        self._file_temp_id = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        self.sms_content = sms_content
        if cids is not None:
            self.cids = cids
        if order_id is not None:
            self.order_id = order_id
        if file_temp_id is not None:
            self.file_temp_id = file_temp_id

    @property
    def template_id(self):
        """Gets the template_id of this CreateSendSmsReq.

        模板id

        :return: The template_id of this CreateSendSmsReq.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateSendSmsReq.

        模板id

        :param template_id: The template_id of this CreateSendSmsReq.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def sms_content(self):
        """Gets the sms_content of this CreateSendSmsReq.

        短信内容

        :return: The sms_content of this CreateSendSmsReq.
        :rtype: str
        """
        return self._sms_content

    @sms_content.setter
    def sms_content(self, sms_content):
        """Sets the sms_content of this CreateSendSmsReq.

        短信内容

        :param sms_content: The sms_content of this CreateSendSmsReq.
        :type sms_content: str
        """
        self._sms_content = sms_content

    @property
    def cids(self):
        """Gets the cids of this CreateSendSmsReq.

        容器ID

        :return: The cids of this CreateSendSmsReq.
        :rtype: list[str]
        """
        return self._cids

    @cids.setter
    def cids(self, cids):
        """Sets the cids of this CreateSendSmsReq.

        容器ID

        :param cids: The cids of this CreateSendSmsReq.
        :type cids: list[str]
        """
        self._cids = cids

    @property
    def order_id(self):
        """Gets the order_id of this CreateSendSmsReq.

        批次号

        :return: The order_id of this CreateSendSmsReq.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CreateSendSmsReq.

        批次号

        :param order_id: The order_id of this CreateSendSmsReq.
        :type order_id: int
        """
        self._order_id = order_id

    @property
    def file_temp_id(self):
        """Gets the file_temp_id of this CreateSendSmsReq.

        临时文件ID

        :return: The file_temp_id of this CreateSendSmsReq.
        :rtype: int
        """
        return self._file_temp_id

    @file_temp_id.setter
    def file_temp_id(self, file_temp_id):
        """Sets the file_temp_id of this CreateSendSmsReq.

        临时文件ID

        :param file_temp_id: The file_temp_id of this CreateSendSmsReq.
        :type file_temp_id: int
        """
        self._file_temp_id = file_temp_id

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
        if not isinstance(other, CreateSendSmsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
