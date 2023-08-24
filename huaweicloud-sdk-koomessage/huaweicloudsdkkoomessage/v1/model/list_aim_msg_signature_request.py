# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimMsgSignatureRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'signature_id': 'str',
        'signature_name': 'str',
        'signature_type': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'limit': 'int',
        'offset': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'signature_id': 'signature_id',
        'signature_name': 'signature_name',
        'signature_type': 'signature_type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, app_name=None, signature_id=None, signature_name=None, signature_type=None, begin_time=None, end_time=None, status=None, limit=None, offset=None):
        """ListAimMsgSignatureRequest

        The model defined in huaweicloud sdk

        :param app_name: 应用名称。
        :type app_name: str
        :param signature_id: 签名ID。
        :type signature_id: str
        :param signature_name: 签名名称。
        :type signature_name: str
        :param signature_type: 签名类型。
        :type signature_type: str
        :param begin_time: 开始时间。
        :type begin_time: str
        :param end_time: 结束时间。
        :type end_time: str
        :param status: 状态。
        :type status: str
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: str
        """
        
        

        self._app_name = None
        self._signature_id = None
        self._signature_name = None
        self._signature_type = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if signature_id is not None:
            self.signature_id = signature_id
        if signature_name is not None:
            self.signature_name = signature_name
        if signature_type is not None:
            self.signature_type = signature_type
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def app_name(self):
        """Gets the app_name of this ListAimMsgSignatureRequest.

        应用名称。

        :return: The app_name of this ListAimMsgSignatureRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListAimMsgSignatureRequest.

        应用名称。

        :param app_name: The app_name of this ListAimMsgSignatureRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def signature_id(self):
        """Gets the signature_id of this ListAimMsgSignatureRequest.

        签名ID。

        :return: The signature_id of this ListAimMsgSignatureRequest.
        :rtype: str
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        """Sets the signature_id of this ListAimMsgSignatureRequest.

        签名ID。

        :param signature_id: The signature_id of this ListAimMsgSignatureRequest.
        :type signature_id: str
        """
        self._signature_id = signature_id

    @property
    def signature_name(self):
        """Gets the signature_name of this ListAimMsgSignatureRequest.

        签名名称。

        :return: The signature_name of this ListAimMsgSignatureRequest.
        :rtype: str
        """
        return self._signature_name

    @signature_name.setter
    def signature_name(self, signature_name):
        """Sets the signature_name of this ListAimMsgSignatureRequest.

        签名名称。

        :param signature_name: The signature_name of this ListAimMsgSignatureRequest.
        :type signature_name: str
        """
        self._signature_name = signature_name

    @property
    def signature_type(self):
        """Gets the signature_type of this ListAimMsgSignatureRequest.

        签名类型。

        :return: The signature_type of this ListAimMsgSignatureRequest.
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this ListAimMsgSignatureRequest.

        签名类型。

        :param signature_type: The signature_type of this ListAimMsgSignatureRequest.
        :type signature_type: str
        """
        self._signature_type = signature_type

    @property
    def begin_time(self):
        """Gets the begin_time of this ListAimMsgSignatureRequest.

        开始时间。

        :return: The begin_time of this ListAimMsgSignatureRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListAimMsgSignatureRequest.

        开始时间。

        :param begin_time: The begin_time of this ListAimMsgSignatureRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAimMsgSignatureRequest.

        结束时间。

        :return: The end_time of this ListAimMsgSignatureRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAimMsgSignatureRequest.

        结束时间。

        :param end_time: The end_time of this ListAimMsgSignatureRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ListAimMsgSignatureRequest.

        状态。

        :return: The status of this ListAimMsgSignatureRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAimMsgSignatureRequest.

        状态。

        :param status: The status of this ListAimMsgSignatureRequest.
        :type status: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this ListAimMsgSignatureRequest.

        每页显示的条目数量。

        :return: The limit of this ListAimMsgSignatureRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAimMsgSignatureRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListAimMsgSignatureRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAimMsgSignatureRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ListAimMsgSignatureRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAimMsgSignatureRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ListAimMsgSignatureRequest.
        :type offset: str
        """
        self._offset = offset

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
        if not isinstance(other, ListAimMsgSignatureRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
