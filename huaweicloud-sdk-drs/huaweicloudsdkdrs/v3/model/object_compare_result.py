# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectCompareResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compare_task_id': 'str',
        'object_compare_overview': 'list[ObjectCompareResultOverview]',
        'object_compare_details': 'dict(str, list[ObjectCompareResultDetails])',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'compare_task_id': 'compare_task_id',
        'object_compare_overview': 'object_compare_overview',
        'object_compare_details': 'object_compare_details',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, compare_task_id=None, object_compare_overview=None, object_compare_details=None, error_code=None, error_msg=None):
        r"""ObjectCompareResult

        The model defined in huaweicloud sdk

        :param compare_task_id: 对象级对比任务的id。
        :type compare_task_id: str
        :param object_compare_overview: 对象对比结果概览。
        :type object_compare_overview: list[:class:`huaweicloudsdkdrs.v3.ObjectCompareResultOverview`]
        :param object_compare_details: 对象对比结果详情。KEY值为对象对比结果概览中的对象类型。
        :type object_compare_details: dict(str, list[ObjectCompareResultDetails])
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误信息。
        :type error_msg: str
        """
        
        

        self._compare_task_id = None
        self._object_compare_overview = None
        self._object_compare_details = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        self.compare_task_id = compare_task_id
        if object_compare_overview is not None:
            self.object_compare_overview = object_compare_overview
        if object_compare_details is not None:
            self.object_compare_details = object_compare_details
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def compare_task_id(self):
        r"""Gets the compare_task_id of this ObjectCompareResult.

        对象级对比任务的id。

        :return: The compare_task_id of this ObjectCompareResult.
        :rtype: str
        """
        return self._compare_task_id

    @compare_task_id.setter
    def compare_task_id(self, compare_task_id):
        r"""Sets the compare_task_id of this ObjectCompareResult.

        对象级对比任务的id。

        :param compare_task_id: The compare_task_id of this ObjectCompareResult.
        :type compare_task_id: str
        """
        self._compare_task_id = compare_task_id

    @property
    def object_compare_overview(self):
        r"""Gets the object_compare_overview of this ObjectCompareResult.

        对象对比结果概览。

        :return: The object_compare_overview of this ObjectCompareResult.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ObjectCompareResultOverview`]
        """
        return self._object_compare_overview

    @object_compare_overview.setter
    def object_compare_overview(self, object_compare_overview):
        r"""Sets the object_compare_overview of this ObjectCompareResult.

        对象对比结果概览。

        :param object_compare_overview: The object_compare_overview of this ObjectCompareResult.
        :type object_compare_overview: list[:class:`huaweicloudsdkdrs.v3.ObjectCompareResultOverview`]
        """
        self._object_compare_overview = object_compare_overview

    @property
    def object_compare_details(self):
        r"""Gets the object_compare_details of this ObjectCompareResult.

        对象对比结果详情。KEY值为对象对比结果概览中的对象类型。

        :return: The object_compare_details of this ObjectCompareResult.
        :rtype: dict(str, list[ObjectCompareResultDetails])
        """
        return self._object_compare_details

    @object_compare_details.setter
    def object_compare_details(self, object_compare_details):
        r"""Sets the object_compare_details of this ObjectCompareResult.

        对象对比结果详情。KEY值为对象对比结果概览中的对象类型。

        :param object_compare_details: The object_compare_details of this ObjectCompareResult.
        :type object_compare_details: dict(str, list[ObjectCompareResultDetails])
        """
        self._object_compare_details = object_compare_details

    @property
    def error_code(self):
        r"""Gets the error_code of this ObjectCompareResult.

        错误码。

        :return: The error_code of this ObjectCompareResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ObjectCompareResult.

        错误码。

        :param error_code: The error_code of this ObjectCompareResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ObjectCompareResult.

        错误信息。

        :return: The error_msg of this ObjectCompareResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ObjectCompareResult.

        错误信息。

        :param error_msg: The error_msg of this ObjectCompareResult.
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
        if not isinstance(other, ObjectCompareResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
