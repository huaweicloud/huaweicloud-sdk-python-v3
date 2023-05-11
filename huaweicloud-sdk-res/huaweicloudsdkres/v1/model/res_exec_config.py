# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResExecConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spark_calc_spec': 'SparkCalcSpec',
        'spark_option_confs': 'list[SparkOptionConf]'
    }

    attribute_map = {
        'spark_calc_spec': 'spark_calc_spec',
        'spark_option_confs': 'spark_option_confs'
    }

    def __init__(self, spark_calc_spec=None, spark_option_confs=None):
        """ResExecConfig

        The model defined in huaweicloud sdk

        :param spark_calc_spec: 
        :type spark_calc_spec: :class:`huaweicloudsdkres.v1.SparkCalcSpec`
        :param spark_option_confs: spark可选配置项
        :type spark_option_confs: list[:class:`huaweicloudsdkres.v1.SparkOptionConf`]
        """
        
        

        self._spark_calc_spec = None
        self._spark_option_confs = None
        self.discriminator = None

        if spark_calc_spec is not None:
            self.spark_calc_spec = spark_calc_spec
        if spark_option_confs is not None:
            self.spark_option_confs = spark_option_confs

    @property
    def spark_calc_spec(self):
        """Gets the spark_calc_spec of this ResExecConfig.

        :return: The spark_calc_spec of this ResExecConfig.
        :rtype: :class:`huaweicloudsdkres.v1.SparkCalcSpec`
        """
        return self._spark_calc_spec

    @spark_calc_spec.setter
    def spark_calc_spec(self, spark_calc_spec):
        """Sets the spark_calc_spec of this ResExecConfig.

        :param spark_calc_spec: The spark_calc_spec of this ResExecConfig.
        :type spark_calc_spec: :class:`huaweicloudsdkres.v1.SparkCalcSpec`
        """
        self._spark_calc_spec = spark_calc_spec

    @property
    def spark_option_confs(self):
        """Gets the spark_option_confs of this ResExecConfig.

        spark可选配置项

        :return: The spark_option_confs of this ResExecConfig.
        :rtype: list[:class:`huaweicloudsdkres.v1.SparkOptionConf`]
        """
        return self._spark_option_confs

    @spark_option_confs.setter
    def spark_option_confs(self, spark_option_confs):
        """Sets the spark_option_confs of this ResExecConfig.

        spark可选配置项

        :param spark_option_confs: The spark_option_confs of this ResExecConfig.
        :type spark_option_confs: list[:class:`huaweicloudsdkres.v1.SparkOptionConf`]
        """
        self._spark_option_confs = spark_option_confs

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
        if not isinstance(other, ResExecConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
