# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubmitDiagnoseJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'params': 'dict(str, str)',
        'region_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'params': 'params',
        'region_id': 'region_id'
    }

    def __init__(self, type=None, params=None, region_id=None):
        """SubmitDiagnoseJobReq

        The model defined in huaweicloud sdk

        :param type: 任务类型，例如 ecs诊断任务 1，rds诊断任务 2
        :type type: int
        :param params: 类型对应的特有参数，例如ecs需要传eip,rds 需要传输instanceId
        :type params: dict(str, str)
        :param region_id: 节点id
        :type region_id: str
        """
        
        

        self._type = None
        self._params = None
        self._region_id = None
        self.discriminator = None

        self.type = type
        if params is not None:
            self.params = params
        if region_id is not None:
            self.region_id = region_id

    @property
    def type(self):
        """Gets the type of this SubmitDiagnoseJobReq.

        任务类型，例如 ecs诊断任务 1，rds诊断任务 2

        :return: The type of this SubmitDiagnoseJobReq.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubmitDiagnoseJobReq.

        任务类型，例如 ecs诊断任务 1，rds诊断任务 2

        :param type: The type of this SubmitDiagnoseJobReq.
        :type type: int
        """
        self._type = type

    @property
    def params(self):
        """Gets the params of this SubmitDiagnoseJobReq.

        类型对应的特有参数，例如ecs需要传eip,rds 需要传输instanceId

        :return: The params of this SubmitDiagnoseJobReq.
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this SubmitDiagnoseJobReq.

        类型对应的特有参数，例如ecs需要传eip,rds 需要传输instanceId

        :param params: The params of this SubmitDiagnoseJobReq.
        :type params: dict(str, str)
        """
        self._params = params

    @property
    def region_id(self):
        """Gets the region_id of this SubmitDiagnoseJobReq.

        节点id

        :return: The region_id of this SubmitDiagnoseJobReq.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this SubmitDiagnoseJobReq.

        节点id

        :param region_id: The region_id of this SubmitDiagnoseJobReq.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, SubmitDiagnoseJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
