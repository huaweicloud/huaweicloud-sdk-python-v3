# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesInfoDiagnosisRequest:

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
        'diagnosis': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'engine': 'engine',
        'diagnosis': 'diagnosis',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, engine=None, diagnosis=None, offset=None, limit=None):
        r"""ListInstancesInfoDiagnosisRequest

        The model defined in huaweicloud sdk

        :param engine: 引擎类型
        :type engine: str
        :param diagnosis: 诊断项
        :type diagnosis: str
        :param offset: offset
        :type offset: int
        :param limit: limit
        :type limit: int
        """
        
        

        self._engine = None
        self._diagnosis = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.engine = engine
        self.diagnosis = diagnosis
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def engine(self):
        r"""Gets the engine of this ListInstancesInfoDiagnosisRequest.

        引擎类型

        :return: The engine of this ListInstancesInfoDiagnosisRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListInstancesInfoDiagnosisRequest.

        引擎类型

        :param engine: The engine of this ListInstancesInfoDiagnosisRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def diagnosis(self):
        r"""Gets the diagnosis of this ListInstancesInfoDiagnosisRequest.

        诊断项

        :return: The diagnosis of this ListInstancesInfoDiagnosisRequest.
        :rtype: str
        """
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        r"""Sets the diagnosis of this ListInstancesInfoDiagnosisRequest.

        诊断项

        :param diagnosis: The diagnosis of this ListInstancesInfoDiagnosisRequest.
        :type diagnosis: str
        """
        self._diagnosis = diagnosis

    @property
    def offset(self):
        r"""Gets the offset of this ListInstancesInfoDiagnosisRequest.

        offset

        :return: The offset of this ListInstancesInfoDiagnosisRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstancesInfoDiagnosisRequest.

        offset

        :param offset: The offset of this ListInstancesInfoDiagnosisRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstancesInfoDiagnosisRequest.

        limit

        :return: The limit of this ListInstancesInfoDiagnosisRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstancesInfoDiagnosisRequest.

        limit

        :param limit: The limit of this ListInstancesInfoDiagnosisRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListInstancesInfoDiagnosisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
