# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePublicipBandwidthOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'str',
        'id': 'str',
        'name': 'str',
        'share_type': 'str',
        'size': 'int'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'id': 'id',
        'name': 'name',
        'share_type': 'share_type',
        'size': 'size'
    }

    def __init__(self, charge_mode=None, id=None, name=None, share_type=None, size=None):
        """CreatePublicipBandwidthOption

        The model defined in huaweicloud sdk

        :param charge_mode: 功能说明：按流量计费还是按带宽计费。 取值范围：bandwidth，traffic。  不填或为空时默认是bandwidth。  其中IPv6国外默认是bandwidth，国内默认是traffic。取值为traffic，表示流量计费。
        :type charge_mode: str
        :param id: 功能说明：带宽ID  创建WHOLE类型带宽的弹性公网IP时可以指定之前的共享带宽创建  取值范围：WHOLE类型的带宽ID 
        :type id: str
        :param name: 功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  如果share_type是PER，该参数必须带,如果share_type是WHOLE并且id有值，该参数会忽略。
        :type name: str
        :param share_type: 功能说明：带宽类型 取值范围：PER，WHOLE(PER为独占带宽，WHOLE是共享带宽)。 约束：该字段为WHOLE时，必须指定带宽ID。
        :type share_type: str
        :param size: 功能说明：带宽大小  取值范围：默认1Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。  约束：share_type是PER，该参数必须带，如果share_type是WHOLE并且id有值，该参数会忽略。  注意：调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。
        :type size: int
        """
        
        

        self._charge_mode = None
        self._id = None
        self._name = None
        self._share_type = None
        self._size = None
        self.discriminator = None

        if charge_mode is not None:
            self.charge_mode = charge_mode
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self.share_type = share_type
        if size is not None:
            self.size = size

    @property
    def charge_mode(self):
        """Gets the charge_mode of this CreatePublicipBandwidthOption.

        功能说明：按流量计费还是按带宽计费。 取值范围：bandwidth，traffic。  不填或为空时默认是bandwidth。  其中IPv6国外默认是bandwidth，国内默认是traffic。取值为traffic，表示流量计费。

        :return: The charge_mode of this CreatePublicipBandwidthOption.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this CreatePublicipBandwidthOption.

        功能说明：按流量计费还是按带宽计费。 取值范围：bandwidth，traffic。  不填或为空时默认是bandwidth。  其中IPv6国外默认是bandwidth，国内默认是traffic。取值为traffic，表示流量计费。

        :param charge_mode: The charge_mode of this CreatePublicipBandwidthOption.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def id(self):
        """Gets the id of this CreatePublicipBandwidthOption.

        功能说明：带宽ID  创建WHOLE类型带宽的弹性公网IP时可以指定之前的共享带宽创建  取值范围：WHOLE类型的带宽ID 

        :return: The id of this CreatePublicipBandwidthOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatePublicipBandwidthOption.

        功能说明：带宽ID  创建WHOLE类型带宽的弹性公网IP时可以指定之前的共享带宽创建  取值范围：WHOLE类型的带宽ID 

        :param id: The id of this CreatePublicipBandwidthOption.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreatePublicipBandwidthOption.

        功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  如果share_type是PER，该参数必须带,如果share_type是WHOLE并且id有值，该参数会忽略。

        :return: The name of this CreatePublicipBandwidthOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePublicipBandwidthOption.

        功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  如果share_type是PER，该参数必须带,如果share_type是WHOLE并且id有值，该参数会忽略。

        :param name: The name of this CreatePublicipBandwidthOption.
        :type name: str
        """
        self._name = name

    @property
    def share_type(self):
        """Gets the share_type of this CreatePublicipBandwidthOption.

        功能说明：带宽类型 取值范围：PER，WHOLE(PER为独占带宽，WHOLE是共享带宽)。 约束：该字段为WHOLE时，必须指定带宽ID。

        :return: The share_type of this CreatePublicipBandwidthOption.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this CreatePublicipBandwidthOption.

        功能说明：带宽类型 取值范围：PER，WHOLE(PER为独占带宽，WHOLE是共享带宽)。 约束：该字段为WHOLE时，必须指定带宽ID。

        :param share_type: The share_type of this CreatePublicipBandwidthOption.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def size(self):
        """Gets the size of this CreatePublicipBandwidthOption.

        功能说明：带宽大小  取值范围：默认1Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。  约束：share_type是PER，该参数必须带，如果share_type是WHOLE并且id有值，该参数会忽略。  注意：调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。

        :return: The size of this CreatePublicipBandwidthOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreatePublicipBandwidthOption.

        功能说明：带宽大小  取值范围：默认1Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。  约束：share_type是PER，该参数必须带，如果share_type是WHOLE并且id有值，该参数会忽略。  注意：调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。

        :param size: The size of this CreatePublicipBandwidthOption.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, CreatePublicipBandwidthOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
