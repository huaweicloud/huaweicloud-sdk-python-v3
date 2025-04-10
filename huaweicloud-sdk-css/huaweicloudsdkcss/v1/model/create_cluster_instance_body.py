# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterInstanceBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'volume': 'CreateClusterInstanceVolumeBody',
        'nics': 'CreateClusterInstanceNicsBody',
        'availability_zone': 'str'
    }

    attribute_map = {
        'flavor_ref': 'flavorRef',
        'volume': 'volume',
        'nics': 'nics',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, flavor_ref=None, volume=None, nics=None, availability_zone=None):
        r"""CreateClusterInstanceBody

        The model defined in huaweicloud sdk

        :param flavor_ref: 实例规格名称。可以使用[获取实例规格列表](ListFlavors.xml)的name属性确认当前拥有的规格信息。
        :type flavor_ref: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkcss.v1.CreateClusterInstanceVolumeBody`
        :param nics: 
        :type nics: :class:`huaweicloudsdkcss.v1.CreateClusterInstanceNicsBody`
        :param availability_zone: 可用区。需要指定可用区的名称（可用分区名称）。 默认指定单AZ。指定多AZ时，各个可用分区名称需要使用英文逗号（,）分隔，以“华北-北京四”为例，选择三AZ时，availability_zone取值为cn-north-4a,cn-north-4b,cn-north-4c。如果使用单AZ，availability_zone默认取值为空。 &gt;说明   选择多AZ时，各个可用分区名称不能重复输入，并且要求节点个数大于等于AZ个数。      如果节点个数为AZ个数的倍数，节点将会均匀的分布到各个AZ。如果节点个数不为AZ个数的倍数时，各个AZ分布的节点数量之差的绝对值小于等于1。     可用分区名称，请在[[地区和终端节点](https://developer.huaweicloud.com/endpoint?CSS)](tag:hws)[[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CSS)](tag:hk_hws)获取。
        :type availability_zone: str
        """
        
        

        self._flavor_ref = None
        self._volume = None
        self._nics = None
        self._availability_zone = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        self.volume = volume
        self.nics = nics
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this CreateClusterInstanceBody.

        实例规格名称。可以使用[获取实例规格列表](ListFlavors.xml)的name属性确认当前拥有的规格信息。

        :return: The flavor_ref of this CreateClusterInstanceBody.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this CreateClusterInstanceBody.

        实例规格名称。可以使用[获取实例规格列表](ListFlavors.xml)的name属性确认当前拥有的规格信息。

        :param flavor_ref: The flavor_ref of this CreateClusterInstanceBody.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        r"""Gets the volume of this CreateClusterInstanceBody.

        :return: The volume of this CreateClusterInstanceBody.
        :rtype: :class:`huaweicloudsdkcss.v1.CreateClusterInstanceVolumeBody`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this CreateClusterInstanceBody.

        :param volume: The volume of this CreateClusterInstanceBody.
        :type volume: :class:`huaweicloudsdkcss.v1.CreateClusterInstanceVolumeBody`
        """
        self._volume = volume

    @property
    def nics(self):
        r"""Gets the nics of this CreateClusterInstanceBody.

        :return: The nics of this CreateClusterInstanceBody.
        :rtype: :class:`huaweicloudsdkcss.v1.CreateClusterInstanceNicsBody`
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        r"""Sets the nics of this CreateClusterInstanceBody.

        :param nics: The nics of this CreateClusterInstanceBody.
        :type nics: :class:`huaweicloudsdkcss.v1.CreateClusterInstanceNicsBody`
        """
        self._nics = nics

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateClusterInstanceBody.

        可用区。需要指定可用区的名称（可用分区名称）。 默认指定单AZ。指定多AZ时，各个可用分区名称需要使用英文逗号（,）分隔，以“华北-北京四”为例，选择三AZ时，availability_zone取值为cn-north-4a,cn-north-4b,cn-north-4c。如果使用单AZ，availability_zone默认取值为空。 >说明   选择多AZ时，各个可用分区名称不能重复输入，并且要求节点个数大于等于AZ个数。      如果节点个数为AZ个数的倍数，节点将会均匀的分布到各个AZ。如果节点个数不为AZ个数的倍数时，各个AZ分布的节点数量之差的绝对值小于等于1。     可用分区名称，请在[[地区和终端节点](https://developer.huaweicloud.com/endpoint?CSS)](tag:hws)[[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CSS)](tag:hk_hws)获取。

        :return: The availability_zone of this CreateClusterInstanceBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateClusterInstanceBody.

        可用区。需要指定可用区的名称（可用分区名称）。 默认指定单AZ。指定多AZ时，各个可用分区名称需要使用英文逗号（,）分隔，以“华北-北京四”为例，选择三AZ时，availability_zone取值为cn-north-4a,cn-north-4b,cn-north-4c。如果使用单AZ，availability_zone默认取值为空。 >说明   选择多AZ时，各个可用分区名称不能重复输入，并且要求节点个数大于等于AZ个数。      如果节点个数为AZ个数的倍数，节点将会均匀的分布到各个AZ。如果节点个数不为AZ个数的倍数时，各个AZ分布的节点数量之差的绝对值小于等于1。     可用分区名称，请在[[地区和终端节点](https://developer.huaweicloud.com/endpoint?CSS)](tag:hws)[[地区和终端节点](https://developer.huaweicloud.com/intl/zh-cn/endpoint?CSS)](tag:hk_hws)获取。

        :param availability_zone: The availability_zone of this CreateClusterInstanceBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, CreateClusterInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
