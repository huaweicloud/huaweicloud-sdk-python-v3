# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessingConfigDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'validity': 'PointValidityingDTO',
        'stream_formula': 'str',
        'scaling': 'PointScalingDTO',
        'clean': 'PointCleanDTO'
    }

    attribute_map = {
        'validity': 'validity',
        'stream_formula': 'stream_formula',
        'scaling': 'scaling',
        'clean': 'clean'
    }

    def __init__(self, validity=None, stream_formula=None, scaling=None, clean=None):
        r"""ProcessingConfigDTO

        The model defined in huaweicloud sdk

        :param validity: 
        :type validity: :class:`huaweicloudsdkiotedge.v2.PointValidityingDTO`
        :param stream_formula: 点位流公式配置字段
        :type stream_formula: str
        :param scaling: 
        :type scaling: :class:`huaweicloudsdkiotedge.v2.PointScalingDTO`
        :param clean: 
        :type clean: :class:`huaweicloudsdkiotedge.v2.PointCleanDTO`
        """
        
        

        self._validity = None
        self._stream_formula = None
        self._scaling = None
        self._clean = None
        self.discriminator = None

        if validity is not None:
            self.validity = validity
        if stream_formula is not None:
            self.stream_formula = stream_formula
        if scaling is not None:
            self.scaling = scaling
        if clean is not None:
            self.clean = clean

    @property
    def validity(self):
        r"""Gets the validity of this ProcessingConfigDTO.

        :return: The validity of this ProcessingConfigDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.PointValidityingDTO`
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        r"""Sets the validity of this ProcessingConfigDTO.

        :param validity: The validity of this ProcessingConfigDTO.
        :type validity: :class:`huaweicloudsdkiotedge.v2.PointValidityingDTO`
        """
        self._validity = validity

    @property
    def stream_formula(self):
        r"""Gets the stream_formula of this ProcessingConfigDTO.

        点位流公式配置字段

        :return: The stream_formula of this ProcessingConfigDTO.
        :rtype: str
        """
        return self._stream_formula

    @stream_formula.setter
    def stream_formula(self, stream_formula):
        r"""Sets the stream_formula of this ProcessingConfigDTO.

        点位流公式配置字段

        :param stream_formula: The stream_formula of this ProcessingConfigDTO.
        :type stream_formula: str
        """
        self._stream_formula = stream_formula

    @property
    def scaling(self):
        r"""Gets the scaling of this ProcessingConfigDTO.

        :return: The scaling of this ProcessingConfigDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.PointScalingDTO`
        """
        return self._scaling

    @scaling.setter
    def scaling(self, scaling):
        r"""Sets the scaling of this ProcessingConfigDTO.

        :param scaling: The scaling of this ProcessingConfigDTO.
        :type scaling: :class:`huaweicloudsdkiotedge.v2.PointScalingDTO`
        """
        self._scaling = scaling

    @property
    def clean(self):
        r"""Gets the clean of this ProcessingConfigDTO.

        :return: The clean of this ProcessingConfigDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.PointCleanDTO`
        """
        return self._clean

    @clean.setter
    def clean(self, clean):
        r"""Sets the clean of this ProcessingConfigDTO.

        :param clean: The clean of this ProcessingConfigDTO.
        :type clean: :class:`huaweicloudsdkiotedge.v2.PointCleanDTO`
        """
        self._clean = clean

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
        if not isinstance(other, ProcessingConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
