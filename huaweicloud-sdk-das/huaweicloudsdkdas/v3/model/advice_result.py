# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdviceResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message_id': 'str',
        'status_code': 'str',
        'error_code': 'str',
        'error_message': 'str',
        'index_advice': 'list[IndexAdviceInfo]',
        'tuning_advice': 'list[str]',
        'formatted_sql': 'str',
        'original_sql': 'str',
        'explain': 'list[Explain]',
        'tb_pos_infos': 'list[TbPosInfo]',
        'feedback_infos': 'FeedbackInfo'
    }

    attribute_map = {
        'message_id': 'message_id',
        'status_code': 'status_code',
        'error_code': 'error_code',
        'error_message': 'error_message',
        'index_advice': 'index_advice',
        'tuning_advice': 'tuning_advice',
        'formatted_sql': 'formatted_sql',
        'original_sql': 'original_sql',
        'explain': 'explain',
        'tb_pos_infos': 'tb_pos_infos',
        'feedback_infos': 'feedback_infos'
    }

    def __init__(self, message_id=None, status_code=None, error_code=None, error_message=None, index_advice=None, tuning_advice=None, formatted_sql=None, original_sql=None, explain=None, tb_pos_infos=None, feedback_infos=None):
        r"""AdviceResult

        The model defined in huaweicloud sdk

        :param message_id: messageId
        :type message_id: str
        :param status_code: 状态码
        :type status_code: str
        :param error_code: 错误码
        :type error_code: str
        :param error_message: 错误信息
        :type error_message: str
        :param index_advice: 索引建议
        :type index_advice: list[:class:`huaweicloudsdkdas.v3.IndexAdviceInfo`]
        :param tuning_advice: 诊断建议
        :type tuning_advice: list[str]
        :param formatted_sql: 格式化SQL
        :type formatted_sql: str
        :param original_sql: 原始SQL
        :type original_sql: str
        :param explain: 执行计划
        :type explain: list[:class:`huaweicloudsdkdas.v3.Explain`]
        :param tb_pos_infos: 表位置信息
        :type tb_pos_infos: list[:class:`huaweicloudsdkdas.v3.TbPosInfo`]
        :param feedback_infos: 
        :type feedback_infos: :class:`huaweicloudsdkdas.v3.FeedbackInfo`
        """
        
        

        self._message_id = None
        self._status_code = None
        self._error_code = None
        self._error_message = None
        self._index_advice = None
        self._tuning_advice = None
        self._formatted_sql = None
        self._original_sql = None
        self._explain = None
        self._tb_pos_infos = None
        self._feedback_infos = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if status_code is not None:
            self.status_code = status_code
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if index_advice is not None:
            self.index_advice = index_advice
        if tuning_advice is not None:
            self.tuning_advice = tuning_advice
        if formatted_sql is not None:
            self.formatted_sql = formatted_sql
        if original_sql is not None:
            self.original_sql = original_sql
        if explain is not None:
            self.explain = explain
        if tb_pos_infos is not None:
            self.tb_pos_infos = tb_pos_infos
        if feedback_infos is not None:
            self.feedback_infos = feedback_infos

    @property
    def message_id(self):
        r"""Gets the message_id of this AdviceResult.

        messageId

        :return: The message_id of this AdviceResult.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        r"""Sets the message_id of this AdviceResult.

        messageId

        :param message_id: The message_id of this AdviceResult.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def status_code(self):
        r"""Gets the status_code of this AdviceResult.

        状态码

        :return: The status_code of this AdviceResult.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this AdviceResult.

        状态码

        :param status_code: The status_code of this AdviceResult.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def error_code(self):
        r"""Gets the error_code of this AdviceResult.

        错误码

        :return: The error_code of this AdviceResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this AdviceResult.

        错误码

        :param error_code: The error_code of this AdviceResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this AdviceResult.

        错误信息

        :return: The error_message of this AdviceResult.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this AdviceResult.

        错误信息

        :param error_message: The error_message of this AdviceResult.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def index_advice(self):
        r"""Gets the index_advice of this AdviceResult.

        索引建议

        :return: The index_advice of this AdviceResult.
        :rtype: list[:class:`huaweicloudsdkdas.v3.IndexAdviceInfo`]
        """
        return self._index_advice

    @index_advice.setter
    def index_advice(self, index_advice):
        r"""Sets the index_advice of this AdviceResult.

        索引建议

        :param index_advice: The index_advice of this AdviceResult.
        :type index_advice: list[:class:`huaweicloudsdkdas.v3.IndexAdviceInfo`]
        """
        self._index_advice = index_advice

    @property
    def tuning_advice(self):
        r"""Gets the tuning_advice of this AdviceResult.

        诊断建议

        :return: The tuning_advice of this AdviceResult.
        :rtype: list[str]
        """
        return self._tuning_advice

    @tuning_advice.setter
    def tuning_advice(self, tuning_advice):
        r"""Sets the tuning_advice of this AdviceResult.

        诊断建议

        :param tuning_advice: The tuning_advice of this AdviceResult.
        :type tuning_advice: list[str]
        """
        self._tuning_advice = tuning_advice

    @property
    def formatted_sql(self):
        r"""Gets the formatted_sql of this AdviceResult.

        格式化SQL

        :return: The formatted_sql of this AdviceResult.
        :rtype: str
        """
        return self._formatted_sql

    @formatted_sql.setter
    def formatted_sql(self, formatted_sql):
        r"""Sets the formatted_sql of this AdviceResult.

        格式化SQL

        :param formatted_sql: The formatted_sql of this AdviceResult.
        :type formatted_sql: str
        """
        self._formatted_sql = formatted_sql

    @property
    def original_sql(self):
        r"""Gets the original_sql of this AdviceResult.

        原始SQL

        :return: The original_sql of this AdviceResult.
        :rtype: str
        """
        return self._original_sql

    @original_sql.setter
    def original_sql(self, original_sql):
        r"""Sets the original_sql of this AdviceResult.

        原始SQL

        :param original_sql: The original_sql of this AdviceResult.
        :type original_sql: str
        """
        self._original_sql = original_sql

    @property
    def explain(self):
        r"""Gets the explain of this AdviceResult.

        执行计划

        :return: The explain of this AdviceResult.
        :rtype: list[:class:`huaweicloudsdkdas.v3.Explain`]
        """
        return self._explain

    @explain.setter
    def explain(self, explain):
        r"""Sets the explain of this AdviceResult.

        执行计划

        :param explain: The explain of this AdviceResult.
        :type explain: list[:class:`huaweicloudsdkdas.v3.Explain`]
        """
        self._explain = explain

    @property
    def tb_pos_infos(self):
        r"""Gets the tb_pos_infos of this AdviceResult.

        表位置信息

        :return: The tb_pos_infos of this AdviceResult.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TbPosInfo`]
        """
        return self._tb_pos_infos

    @tb_pos_infos.setter
    def tb_pos_infos(self, tb_pos_infos):
        r"""Sets the tb_pos_infos of this AdviceResult.

        表位置信息

        :param tb_pos_infos: The tb_pos_infos of this AdviceResult.
        :type tb_pos_infos: list[:class:`huaweicloudsdkdas.v3.TbPosInfo`]
        """
        self._tb_pos_infos = tb_pos_infos

    @property
    def feedback_infos(self):
        r"""Gets the feedback_infos of this AdviceResult.

        :return: The feedback_infos of this AdviceResult.
        :rtype: :class:`huaweicloudsdkdas.v3.FeedbackInfo`
        """
        return self._feedback_infos

    @feedback_infos.setter
    def feedback_infos(self, feedback_infos):
        r"""Sets the feedback_infos of this AdviceResult.

        :param feedback_infos: The feedback_infos of this AdviceResult.
        :type feedback_infos: :class:`huaweicloudsdkdas.v3.FeedbackInfo`
        """
        self._feedback_infos = feedback_infos

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
        if not isinstance(other, AdviceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
