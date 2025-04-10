# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaMessageDiagnosisItemEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'result': 'str',
        'cause_ids': 'list[KafkaMessageDiagnosisConclusionEntity]',
        'advice_ids': 'list[KafkaMessageDiagnosisConclusionEntity]',
        'partitions': 'list[int]',
        'failed_partitions': 'list[int]',
        'broker_ids': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'result': 'result',
        'cause_ids': 'cause_ids',
        'advice_ids': 'advice_ids',
        'partitions': 'partitions',
        'failed_partitions': 'failed_partitions',
        'broker_ids': 'broker_ids'
    }

    def __init__(self, name=None, result=None, cause_ids=None, advice_ids=None, partitions=None, failed_partitions=None, broker_ids=None):
        r"""KafkaMessageDiagnosisItemEntity

        The model defined in huaweicloud sdk

        :param name: 诊断项名称
        :type name: str
        :param result: 诊断结果
        :type result: str
        :param cause_ids: 诊断异常原因列表
        :type cause_ids: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisConclusionEntity`]
        :param advice_ids: 诊断异常建议列表
        :type advice_ids: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisConclusionEntity`]
        :param partitions: 诊断异常受影响的分区列表
        :type partitions: list[int]
        :param failed_partitions: 诊断失败的分区列表
        :type failed_partitions: list[int]
        :param broker_ids: 诊断异常受影响的broker列表
        :type broker_ids: list[int]
        """
        
        

        self._name = None
        self._result = None
        self._cause_ids = None
        self._advice_ids = None
        self._partitions = None
        self._failed_partitions = None
        self._broker_ids = None
        self.discriminator = None

        self.name = name
        self.result = result
        if cause_ids is not None:
            self.cause_ids = cause_ids
        if advice_ids is not None:
            self.advice_ids = advice_ids
        if partitions is not None:
            self.partitions = partitions
        if failed_partitions is not None:
            self.failed_partitions = failed_partitions
        if broker_ids is not None:
            self.broker_ids = broker_ids

    @property
    def name(self):
        r"""Gets the name of this KafkaMessageDiagnosisItemEntity.

        诊断项名称

        :return: The name of this KafkaMessageDiagnosisItemEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KafkaMessageDiagnosisItemEntity.

        诊断项名称

        :param name: The name of this KafkaMessageDiagnosisItemEntity.
        :type name: str
        """
        self._name = name

    @property
    def result(self):
        r"""Gets the result of this KafkaMessageDiagnosisItemEntity.

        诊断结果

        :return: The result of this KafkaMessageDiagnosisItemEntity.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this KafkaMessageDiagnosisItemEntity.

        诊断结果

        :param result: The result of this KafkaMessageDiagnosisItemEntity.
        :type result: str
        """
        self._result = result

    @property
    def cause_ids(self):
        r"""Gets the cause_ids of this KafkaMessageDiagnosisItemEntity.

        诊断异常原因列表

        :return: The cause_ids of this KafkaMessageDiagnosisItemEntity.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisConclusionEntity`]
        """
        return self._cause_ids

    @cause_ids.setter
    def cause_ids(self, cause_ids):
        r"""Sets the cause_ids of this KafkaMessageDiagnosisItemEntity.

        诊断异常原因列表

        :param cause_ids: The cause_ids of this KafkaMessageDiagnosisItemEntity.
        :type cause_ids: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisConclusionEntity`]
        """
        self._cause_ids = cause_ids

    @property
    def advice_ids(self):
        r"""Gets the advice_ids of this KafkaMessageDiagnosisItemEntity.

        诊断异常建议列表

        :return: The advice_ids of this KafkaMessageDiagnosisItemEntity.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisConclusionEntity`]
        """
        return self._advice_ids

    @advice_ids.setter
    def advice_ids(self, advice_ids):
        r"""Sets the advice_ids of this KafkaMessageDiagnosisItemEntity.

        诊断异常建议列表

        :param advice_ids: The advice_ids of this KafkaMessageDiagnosisItemEntity.
        :type advice_ids: list[:class:`huaweicloudsdkkafka.v2.KafkaMessageDiagnosisConclusionEntity`]
        """
        self._advice_ids = advice_ids

    @property
    def partitions(self):
        r"""Gets the partitions of this KafkaMessageDiagnosisItemEntity.

        诊断异常受影响的分区列表

        :return: The partitions of this KafkaMessageDiagnosisItemEntity.
        :rtype: list[int]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        r"""Sets the partitions of this KafkaMessageDiagnosisItemEntity.

        诊断异常受影响的分区列表

        :param partitions: The partitions of this KafkaMessageDiagnosisItemEntity.
        :type partitions: list[int]
        """
        self._partitions = partitions

    @property
    def failed_partitions(self):
        r"""Gets the failed_partitions of this KafkaMessageDiagnosisItemEntity.

        诊断失败的分区列表

        :return: The failed_partitions of this KafkaMessageDiagnosisItemEntity.
        :rtype: list[int]
        """
        return self._failed_partitions

    @failed_partitions.setter
    def failed_partitions(self, failed_partitions):
        r"""Sets the failed_partitions of this KafkaMessageDiagnosisItemEntity.

        诊断失败的分区列表

        :param failed_partitions: The failed_partitions of this KafkaMessageDiagnosisItemEntity.
        :type failed_partitions: list[int]
        """
        self._failed_partitions = failed_partitions

    @property
    def broker_ids(self):
        r"""Gets the broker_ids of this KafkaMessageDiagnosisItemEntity.

        诊断异常受影响的broker列表

        :return: The broker_ids of this KafkaMessageDiagnosisItemEntity.
        :rtype: list[int]
        """
        return self._broker_ids

    @broker_ids.setter
    def broker_ids(self, broker_ids):
        r"""Sets the broker_ids of this KafkaMessageDiagnosisItemEntity.

        诊断异常受影响的broker列表

        :param broker_ids: The broker_ids of this KafkaMessageDiagnosisItemEntity.
        :type broker_ids: list[int]
        """
        self._broker_ids = broker_ids

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
        if not isinstance(other, KafkaMessageDiagnosisItemEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
