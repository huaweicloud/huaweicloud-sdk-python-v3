# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMemberGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'member_group_name': 'str',
        'member_group_remark': 'str',
        'member_group_weight': 'int',
        'dict_code': 'str',
        'microservice_version': 'str',
        'microservice_port': 'int',
        'microservice_labels': 'list[MicroserviceLabel]',
        'reference_vpc_channel_id': 'str',
        'member_group_id': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'member_group_name': 'member_group_name',
        'member_group_remark': 'member_group_remark',
        'member_group_weight': 'member_group_weight',
        'dict_code': 'dict_code',
        'microservice_version': 'microservice_version',
        'microservice_port': 'microservice_port',
        'microservice_labels': 'microservice_labels',
        'reference_vpc_channel_id': 'reference_vpc_channel_id',
        'member_group_id': 'member_group_id',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, member_group_name=None, member_group_remark=None, member_group_weight=None, dict_code=None, microservice_version=None, microservice_port=None, microservice_labels=None, reference_vpc_channel_id=None, member_group_id=None, create_time=None, update_time=None):
        r"""UpdateMemberGroupResponse

        The model defined in huaweicloud sdk

        :param member_group_name: VPC通道后端服务器组名称。支持汉字、英文、数字、下划线、中划线、点，且只能以英文和汉字开头，3-64字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type member_group_name: str
        :param member_group_remark: VPC通道后端服务器组描述。
        :type member_group_remark: str
        :param member_group_weight: VPC通道后端服务器组权重值。  当前服务器组存在服务器且此权重值存在时，自动使用此权重值分配权重。
        :type member_group_weight: int
        :param dict_code: VPC通道后端服务器组的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持
        :type dict_code: str
        :param microservice_version: VPC通道后端服务器组的版本，仅VPC通道类型为微服务时支持。
        :type microservice_version: str
        :param microservice_port: VPC通道后端服务器组的端口号，仅VPC通道类型为微服务时支持。端口号为0时后端服务器组下的所有地址沿用原来负载端口继承逻辑。
        :type microservice_port: int
        :param microservice_labels: VPC通道后端服务器组的标签，仅VPC通道类型为微服务时支持。
        :type microservice_labels: list[:class:`huaweicloudsdkapig.v2.MicroserviceLabel`]
        :param reference_vpc_channel_id: 引用的负载通道编号，仅VPC通道类型为引用类型（vpc_channel_type&#x3D;reference）时支持。
        :type reference_vpc_channel_id: str
        :param member_group_id: VPC通道后端服务器组编号
        :type member_group_id: str
        :param create_time: VPC通道后端服务器组创建时间
        :type create_time: datetime
        :param update_time: VPC通道后端服务器组更新时间
        :type update_time: datetime
        """
        
        super(UpdateMemberGroupResponse, self).__init__()

        self._member_group_name = None
        self._member_group_remark = None
        self._member_group_weight = None
        self._dict_code = None
        self._microservice_version = None
        self._microservice_port = None
        self._microservice_labels = None
        self._reference_vpc_channel_id = None
        self._member_group_id = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.member_group_name = member_group_name
        if member_group_remark is not None:
            self.member_group_remark = member_group_remark
        if member_group_weight is not None:
            self.member_group_weight = member_group_weight
        if dict_code is not None:
            self.dict_code = dict_code
        if microservice_version is not None:
            self.microservice_version = microservice_version
        if microservice_port is not None:
            self.microservice_port = microservice_port
        if microservice_labels is not None:
            self.microservice_labels = microservice_labels
        if reference_vpc_channel_id is not None:
            self.reference_vpc_channel_id = reference_vpc_channel_id
        if member_group_id is not None:
            self.member_group_id = member_group_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def member_group_name(self):
        r"""Gets the member_group_name of this UpdateMemberGroupResponse.

        VPC通道后端服务器组名称。支持汉字、英文、数字、下划线、中划线、点，且只能以英文和汉字开头，3-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The member_group_name of this UpdateMemberGroupResponse.
        :rtype: str
        """
        return self._member_group_name

    @member_group_name.setter
    def member_group_name(self, member_group_name):
        r"""Sets the member_group_name of this UpdateMemberGroupResponse.

        VPC通道后端服务器组名称。支持汉字、英文、数字、下划线、中划线、点，且只能以英文和汉字开头，3-64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param member_group_name: The member_group_name of this UpdateMemberGroupResponse.
        :type member_group_name: str
        """
        self._member_group_name = member_group_name

    @property
    def member_group_remark(self):
        r"""Gets the member_group_remark of this UpdateMemberGroupResponse.

        VPC通道后端服务器组描述。

        :return: The member_group_remark of this UpdateMemberGroupResponse.
        :rtype: str
        """
        return self._member_group_remark

    @member_group_remark.setter
    def member_group_remark(self, member_group_remark):
        r"""Sets the member_group_remark of this UpdateMemberGroupResponse.

        VPC通道后端服务器组描述。

        :param member_group_remark: The member_group_remark of this UpdateMemberGroupResponse.
        :type member_group_remark: str
        """
        self._member_group_remark = member_group_remark

    @property
    def member_group_weight(self):
        r"""Gets the member_group_weight of this UpdateMemberGroupResponse.

        VPC通道后端服务器组权重值。  当前服务器组存在服务器且此权重值存在时，自动使用此权重值分配权重。

        :return: The member_group_weight of this UpdateMemberGroupResponse.
        :rtype: int
        """
        return self._member_group_weight

    @member_group_weight.setter
    def member_group_weight(self, member_group_weight):
        r"""Sets the member_group_weight of this UpdateMemberGroupResponse.

        VPC通道后端服务器组权重值。  当前服务器组存在服务器且此权重值存在时，自动使用此权重值分配权重。

        :param member_group_weight: The member_group_weight of this UpdateMemberGroupResponse.
        :type member_group_weight: int
        """
        self._member_group_weight = member_group_weight

    @property
    def dict_code(self):
        r"""Gets the dict_code of this UpdateMemberGroupResponse.

        VPC通道后端服务器组的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :return: The dict_code of this UpdateMemberGroupResponse.
        :rtype: str
        """
        return self._dict_code

    @dict_code.setter
    def dict_code(self, dict_code):
        r"""Sets the dict_code of this UpdateMemberGroupResponse.

        VPC通道后端服务器组的字典编码  支持英文，数字，特殊字符（-_.）  暂不支持

        :param dict_code: The dict_code of this UpdateMemberGroupResponse.
        :type dict_code: str
        """
        self._dict_code = dict_code

    @property
    def microservice_version(self):
        r"""Gets the microservice_version of this UpdateMemberGroupResponse.

        VPC通道后端服务器组的版本，仅VPC通道类型为微服务时支持。

        :return: The microservice_version of this UpdateMemberGroupResponse.
        :rtype: str
        """
        return self._microservice_version

    @microservice_version.setter
    def microservice_version(self, microservice_version):
        r"""Sets the microservice_version of this UpdateMemberGroupResponse.

        VPC通道后端服务器组的版本，仅VPC通道类型为微服务时支持。

        :param microservice_version: The microservice_version of this UpdateMemberGroupResponse.
        :type microservice_version: str
        """
        self._microservice_version = microservice_version

    @property
    def microservice_port(self):
        r"""Gets the microservice_port of this UpdateMemberGroupResponse.

        VPC通道后端服务器组的端口号，仅VPC通道类型为微服务时支持。端口号为0时后端服务器组下的所有地址沿用原来负载端口继承逻辑。

        :return: The microservice_port of this UpdateMemberGroupResponse.
        :rtype: int
        """
        return self._microservice_port

    @microservice_port.setter
    def microservice_port(self, microservice_port):
        r"""Sets the microservice_port of this UpdateMemberGroupResponse.

        VPC通道后端服务器组的端口号，仅VPC通道类型为微服务时支持。端口号为0时后端服务器组下的所有地址沿用原来负载端口继承逻辑。

        :param microservice_port: The microservice_port of this UpdateMemberGroupResponse.
        :type microservice_port: int
        """
        self._microservice_port = microservice_port

    @property
    def microservice_labels(self):
        r"""Gets the microservice_labels of this UpdateMemberGroupResponse.

        VPC通道后端服务器组的标签，仅VPC通道类型为微服务时支持。

        :return: The microservice_labels of this UpdateMemberGroupResponse.
        :rtype: list[:class:`huaweicloudsdkapig.v2.MicroserviceLabel`]
        """
        return self._microservice_labels

    @microservice_labels.setter
    def microservice_labels(self, microservice_labels):
        r"""Sets the microservice_labels of this UpdateMemberGroupResponse.

        VPC通道后端服务器组的标签，仅VPC通道类型为微服务时支持。

        :param microservice_labels: The microservice_labels of this UpdateMemberGroupResponse.
        :type microservice_labels: list[:class:`huaweicloudsdkapig.v2.MicroserviceLabel`]
        """
        self._microservice_labels = microservice_labels

    @property
    def reference_vpc_channel_id(self):
        r"""Gets the reference_vpc_channel_id of this UpdateMemberGroupResponse.

        引用的负载通道编号，仅VPC通道类型为引用类型（vpc_channel_type=reference）时支持。

        :return: The reference_vpc_channel_id of this UpdateMemberGroupResponse.
        :rtype: str
        """
        return self._reference_vpc_channel_id

    @reference_vpc_channel_id.setter
    def reference_vpc_channel_id(self, reference_vpc_channel_id):
        r"""Sets the reference_vpc_channel_id of this UpdateMemberGroupResponse.

        引用的负载通道编号，仅VPC通道类型为引用类型（vpc_channel_type=reference）时支持。

        :param reference_vpc_channel_id: The reference_vpc_channel_id of this UpdateMemberGroupResponse.
        :type reference_vpc_channel_id: str
        """
        self._reference_vpc_channel_id = reference_vpc_channel_id

    @property
    def member_group_id(self):
        r"""Gets the member_group_id of this UpdateMemberGroupResponse.

        VPC通道后端服务器组编号

        :return: The member_group_id of this UpdateMemberGroupResponse.
        :rtype: str
        """
        return self._member_group_id

    @member_group_id.setter
    def member_group_id(self, member_group_id):
        r"""Sets the member_group_id of this UpdateMemberGroupResponse.

        VPC通道后端服务器组编号

        :param member_group_id: The member_group_id of this UpdateMemberGroupResponse.
        :type member_group_id: str
        """
        self._member_group_id = member_group_id

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateMemberGroupResponse.

        VPC通道后端服务器组创建时间

        :return: The create_time of this UpdateMemberGroupResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateMemberGroupResponse.

        VPC通道后端服务器组创建时间

        :param create_time: The create_time of this UpdateMemberGroupResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateMemberGroupResponse.

        VPC通道后端服务器组更新时间

        :return: The update_time of this UpdateMemberGroupResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateMemberGroupResponse.

        VPC通道后端服务器组更新时间

        :param update_time: The update_time of this UpdateMemberGroupResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, UpdateMemberGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
