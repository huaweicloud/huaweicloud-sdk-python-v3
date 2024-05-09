# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectsCompareDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_db_name': 'str',
        'target_db_name': 'str',
        'source_db_value': 'str',
        'target_db_value': 'str',
        'status': 'int',
        'error_message': 'str'
    }

    attribute_map = {
        'source_db_name': 'source_db_name',
        'target_db_name': 'target_db_name',
        'source_db_value': 'source_db_value',
        'target_db_value': 'target_db_value',
        'status': 'status',
        'error_message': 'error_message'
    }

    def __init__(self, source_db_name=None, target_db_name=None, source_db_value=None, target_db_value=None, status=None, error_message=None):
        """ObjectsCompareDetailInfo

        The model defined in huaweicloud sdk

        :param source_db_name: 源库名称。
        :type source_db_name: str
        :param target_db_name: 目标库名称。
        :type target_db_name: str
        :param source_db_value: 在源库的值。
        :type source_db_value: str
        :param target_db_value: 在目标库的值。
        :type target_db_value: str
        :param status: 对比结果，0为不一致，2为一致，3为未完成。
        :type status: int
        :param error_message: 错误信息。
        :type error_message: str
        """
        
        

        self._source_db_name = None
        self._target_db_name = None
        self._source_db_value = None
        self._target_db_value = None
        self._status = None
        self._error_message = None
        self.discriminator = None

        if source_db_name is not None:
            self.source_db_name = source_db_name
        if target_db_name is not None:
            self.target_db_name = target_db_name
        if source_db_value is not None:
            self.source_db_value = source_db_value
        if target_db_value is not None:
            self.target_db_value = target_db_value
        if status is not None:
            self.status = status
        if error_message is not None:
            self.error_message = error_message

    @property
    def source_db_name(self):
        """Gets the source_db_name of this ObjectsCompareDetailInfo.

        源库名称。

        :return: The source_db_name of this ObjectsCompareDetailInfo.
        :rtype: str
        """
        return self._source_db_name

    @source_db_name.setter
    def source_db_name(self, source_db_name):
        """Sets the source_db_name of this ObjectsCompareDetailInfo.

        源库名称。

        :param source_db_name: The source_db_name of this ObjectsCompareDetailInfo.
        :type source_db_name: str
        """
        self._source_db_name = source_db_name

    @property
    def target_db_name(self):
        """Gets the target_db_name of this ObjectsCompareDetailInfo.

        目标库名称。

        :return: The target_db_name of this ObjectsCompareDetailInfo.
        :rtype: str
        """
        return self._target_db_name

    @target_db_name.setter
    def target_db_name(self, target_db_name):
        """Sets the target_db_name of this ObjectsCompareDetailInfo.

        目标库名称。

        :param target_db_name: The target_db_name of this ObjectsCompareDetailInfo.
        :type target_db_name: str
        """
        self._target_db_name = target_db_name

    @property
    def source_db_value(self):
        """Gets the source_db_value of this ObjectsCompareDetailInfo.

        在源库的值。

        :return: The source_db_value of this ObjectsCompareDetailInfo.
        :rtype: str
        """
        return self._source_db_value

    @source_db_value.setter
    def source_db_value(self, source_db_value):
        """Sets the source_db_value of this ObjectsCompareDetailInfo.

        在源库的值。

        :param source_db_value: The source_db_value of this ObjectsCompareDetailInfo.
        :type source_db_value: str
        """
        self._source_db_value = source_db_value

    @property
    def target_db_value(self):
        """Gets the target_db_value of this ObjectsCompareDetailInfo.

        在目标库的值。

        :return: The target_db_value of this ObjectsCompareDetailInfo.
        :rtype: str
        """
        return self._target_db_value

    @target_db_value.setter
    def target_db_value(self, target_db_value):
        """Sets the target_db_value of this ObjectsCompareDetailInfo.

        在目标库的值。

        :param target_db_value: The target_db_value of this ObjectsCompareDetailInfo.
        :type target_db_value: str
        """
        self._target_db_value = target_db_value

    @property
    def status(self):
        """Gets the status of this ObjectsCompareDetailInfo.

        对比结果，0为不一致，2为一致，3为未完成。

        :return: The status of this ObjectsCompareDetailInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ObjectsCompareDetailInfo.

        对比结果，0为不一致，2为一致，3为未完成。

        :param status: The status of this ObjectsCompareDetailInfo.
        :type status: int
        """
        self._status = status

    @property
    def error_message(self):
        """Gets the error_message of this ObjectsCompareDetailInfo.

        错误信息。

        :return: The error_message of this ObjectsCompareDetailInfo.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ObjectsCompareDetailInfo.

        错误信息。

        :param error_message: The error_message of this ObjectsCompareDetailInfo.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, ObjectsCompareDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
