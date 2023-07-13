# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomPropsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'prop_definition': 'PropDefinition',
        'metrics': 'list[CustomPropsModelMetric]'
    }

    attribute_map = {
        'id': 'id',
        'prop_definition': 'prop_definition',
        'metrics': 'metrics'
    }

    def __init__(self, id=None, prop_definition=None, metrics=None):
        """CustomPropsResult

        The model defined in huaweicloud sdk

        :param id: 自定义属性ID（API侧）
        :type id: str
        :param prop_definition: 
        :type prop_definition: :class:`huaweicloudsdkeihealth.v1.PropDefinition`
        :param metrics: 自定义属性建模的评估指标集合
        :type metrics: list[:class:`huaweicloudsdkeihealth.v1.CustomPropsModelMetric`]
        """
        
        

        self._id = None
        self._prop_definition = None
        self._metrics = None
        self.discriminator = None

        self.id = id
        self.prop_definition = prop_definition
        self.metrics = metrics

    @property
    def id(self):
        """Gets the id of this CustomPropsResult.

        自定义属性ID（API侧）

        :return: The id of this CustomPropsResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomPropsResult.

        自定义属性ID（API侧）

        :param id: The id of this CustomPropsResult.
        :type id: str
        """
        self._id = id

    @property
    def prop_definition(self):
        """Gets the prop_definition of this CustomPropsResult.

        :return: The prop_definition of this CustomPropsResult.
        :rtype: :class:`huaweicloudsdkeihealth.v1.PropDefinition`
        """
        return self._prop_definition

    @prop_definition.setter
    def prop_definition(self, prop_definition):
        """Sets the prop_definition of this CustomPropsResult.

        :param prop_definition: The prop_definition of this CustomPropsResult.
        :type prop_definition: :class:`huaweicloudsdkeihealth.v1.PropDefinition`
        """
        self._prop_definition = prop_definition

    @property
    def metrics(self):
        """Gets the metrics of this CustomPropsResult.

        自定义属性建模的评估指标集合

        :return: The metrics of this CustomPropsResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.CustomPropsModelMetric`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this CustomPropsResult.

        自定义属性建模的评估指标集合

        :param metrics: The metrics of this CustomPropsResult.
        :type metrics: list[:class:`huaweicloudsdkeihealth.v1.CustomPropsModelMetric`]
        """
        self._metrics = metrics

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
        if not isinstance(other, CustomPropsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
