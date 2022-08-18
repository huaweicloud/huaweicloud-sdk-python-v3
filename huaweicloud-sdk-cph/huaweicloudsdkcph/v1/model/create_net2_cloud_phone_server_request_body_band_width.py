# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNet2CloudPhoneServerRequestBodyBandWidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'band_width_share_type': 'int',
        'band_width_size': 'int',
        'band_width_id': 'str'
    }

    attribute_map = {
        'band_width_share_type': 'band_width_share_type',
        'band_width_size': 'band_width_size',
        'band_width_id': 'band_width_id'
    }

    def __init__(self, band_width_share_type=None, band_width_size=None, band_width_id=None):
        """CreateNet2CloudPhoneServerRequestBodyBandWidth

        The model defined in huaweicloud sdk

        :param band_width_share_type: 带宽类型 - 0 表示独享带宽 - 1 表示共享带宽
        :type band_width_share_type: int
        :param band_width_size: 功能说明：带宽大小  带宽（Mbit/s），取值范围为[1,2000]。  调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 大于1000Mbit/s：默认最小单位为500Mbit/s。 说明：  如果share_type是独享带宽，该参数必选项；如果share_type是共享带宽并且id有值，该参数会忽略
        :type band_width_size: int
        :param band_width_id: 带宽ID，创建共享带宽类型带宽的弹性IP时可以指定之前的共享带宽创建。  取值范围：共享带宽类型的带宽ID。  说明：  当创建共享带宽类型的带宽时，该字段必选
        :type band_width_id: str
        """
        
        

        self._band_width_share_type = None
        self._band_width_size = None
        self._band_width_id = None
        self.discriminator = None

        self.band_width_share_type = band_width_share_type
        if band_width_size is not None:
            self.band_width_size = band_width_size
        if band_width_id is not None:
            self.band_width_id = band_width_id

    @property
    def band_width_share_type(self):
        """Gets the band_width_share_type of this CreateNet2CloudPhoneServerRequestBodyBandWidth.

        带宽类型 - 0 表示独享带宽 - 1 表示共享带宽

        :return: The band_width_share_type of this CreateNet2CloudPhoneServerRequestBodyBandWidth.
        :rtype: int
        """
        return self._band_width_share_type

    @band_width_share_type.setter
    def band_width_share_type(self, band_width_share_type):
        """Sets the band_width_share_type of this CreateNet2CloudPhoneServerRequestBodyBandWidth.

        带宽类型 - 0 表示独享带宽 - 1 表示共享带宽

        :param band_width_share_type: The band_width_share_type of this CreateNet2CloudPhoneServerRequestBodyBandWidth.
        :type band_width_share_type: int
        """
        self._band_width_share_type = band_width_share_type

    @property
    def band_width_size(self):
        """Gets the band_width_size of this CreateNet2CloudPhoneServerRequestBodyBandWidth.

        功能说明：带宽大小  带宽（Mbit/s），取值范围为[1,2000]。  调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 大于1000Mbit/s：默认最小单位为500Mbit/s。 说明：  如果share_type是独享带宽，该参数必选项；如果share_type是共享带宽并且id有值，该参数会忽略

        :return: The band_width_size of this CreateNet2CloudPhoneServerRequestBodyBandWidth.
        :rtype: int
        """
        return self._band_width_size

    @band_width_size.setter
    def band_width_size(self, band_width_size):
        """Sets the band_width_size of this CreateNet2CloudPhoneServerRequestBodyBandWidth.

        功能说明：带宽大小  带宽（Mbit/s），取值范围为[1,2000]。  调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 大于1000Mbit/s：默认最小单位为500Mbit/s。 说明：  如果share_type是独享带宽，该参数必选项；如果share_type是共享带宽并且id有值，该参数会忽略

        :param band_width_size: The band_width_size of this CreateNet2CloudPhoneServerRequestBodyBandWidth.
        :type band_width_size: int
        """
        self._band_width_size = band_width_size

    @property
    def band_width_id(self):
        """Gets the band_width_id of this CreateNet2CloudPhoneServerRequestBodyBandWidth.

        带宽ID，创建共享带宽类型带宽的弹性IP时可以指定之前的共享带宽创建。  取值范围：共享带宽类型的带宽ID。  说明：  当创建共享带宽类型的带宽时，该字段必选

        :return: The band_width_id of this CreateNet2CloudPhoneServerRequestBodyBandWidth.
        :rtype: str
        """
        return self._band_width_id

    @band_width_id.setter
    def band_width_id(self, band_width_id):
        """Sets the band_width_id of this CreateNet2CloudPhoneServerRequestBodyBandWidth.

        带宽ID，创建共享带宽类型带宽的弹性IP时可以指定之前的共享带宽创建。  取值范围：共享带宽类型的带宽ID。  说明：  当创建共享带宽类型的带宽时，该字段必选

        :param band_width_id: The band_width_id of this CreateNet2CloudPhoneServerRequestBodyBandWidth.
        :type band_width_id: str
        """
        self._band_width_id = band_width_id

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
        if not isinstance(other, CreateNet2CloudPhoneServerRequestBodyBandWidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
