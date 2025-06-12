# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteDiagnosisReportRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'instance_id': 'str',
        'body': 'BatchDeleteDiagnosisReportReq'
    }

    attribute_map = {
        'engine': 'engine',
        'instance_id': 'instance_id',
        'body': 'body'
    }

    def __init__(self, engine=None, instance_id=None, body=None):
        r"""BatchDeleteDiagnosisReportRequest

        The model defined in huaweicloud sdk

        :param engine: **参数解释**： 引擎。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type engine: str
        :param instance_id: **参数解释**： 实例ID。获取方法如下：登录RocketMQ控制台，在RocketMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type instance_id: str
        :param body: Body of the BatchDeleteDiagnosisReportRequest
        :type body: :class:`huaweicloudsdkrocketmq.v2.BatchDeleteDiagnosisReportReq`
        """
        
        

        self._engine = None
        self._instance_id = None
        self._body = None
        self.discriminator = None

        self.engine = engine
        self.instance_id = instance_id
        if body is not None:
            self.body = body

    @property
    def engine(self):
        r"""Gets the engine of this BatchDeleteDiagnosisReportRequest.

        **参数解释**： 引擎。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The engine of this BatchDeleteDiagnosisReportRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this BatchDeleteDiagnosisReportRequest.

        **参数解释**： 引擎。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param engine: The engine of this BatchDeleteDiagnosisReportRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BatchDeleteDiagnosisReportRequest.

        **参数解释**： 实例ID。获取方法如下：登录RocketMQ控制台，在RocketMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_id of this BatchDeleteDiagnosisReportRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BatchDeleteDiagnosisReportRequest.

        **参数解释**： 实例ID。获取方法如下：登录RocketMQ控制台，在RocketMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param instance_id: The instance_id of this BatchDeleteDiagnosisReportRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def body(self):
        r"""Gets the body of this BatchDeleteDiagnosisReportRequest.

        :return: The body of this BatchDeleteDiagnosisReportRequest.
        :rtype: :class:`huaweicloudsdkrocketmq.v2.BatchDeleteDiagnosisReportReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchDeleteDiagnosisReportRequest.

        :param body: The body of this BatchDeleteDiagnosisReportRequest.
        :type body: :class:`huaweicloudsdkrocketmq.v2.BatchDeleteDiagnosisReportReq`
        """
        self._body = body

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
        if not isinstance(other, BatchDeleteDiagnosisReportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
