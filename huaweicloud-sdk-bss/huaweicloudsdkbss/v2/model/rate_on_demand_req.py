# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RateOnDemandReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'inquiry_precision': 'int',
        'product_infos': 'list[DemandProductInfo]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'inquiry_precision': 'inquiry_precision',
        'product_infos': 'product_infos'
    }

    def __init__(self, project_id=None, inquiry_precision=None, product_infos=None):
        """RateOnDemandReq

        The model defined in huaweicloud sdk

        :param project_id: 项目ID。  说明： 使用客户Token，可以调用[通过assume_role方式获取用户token](https://support.huaweicloud.com/api-iam/iam_30_0003.html)接口获取“regionId”的取值对应的“project id”。具体请参见[如何将合作伙伴Token置换为客户Token](https://support.huaweicloud.com/bpconsole_faq/bpconsole_apifaq_00001.html)的步骤2。IAM子用户调用此接口，需要IAM主账号授权，具体请参考[创建用户组并授权](https://support.huaweicloud.com/usermanual-iam/iam_03_0001.html)。
        :type project_id: str
        :param inquiry_precision: 查询价格结果的精度模式。 0：询价结果默认精度截取，即最长保留到元后6位小数点，如0.000001元1：询价结果保留10位精度，即最长保留到元后10位小数点，如1.0000000001元  说明： 如果询价结果只到元后2位或者3位，那么价格也只到元后2位或者3位，不管传0或者传1都一样，只有询价结果到了小数点后面6位以上，传0和传1才有区别。
        :type inquiry_precision: int
        :param product_infos: 产品信息列表，询价时要询价产品的信息的列表，具体参见表1。
        :type product_infos: list[:class:`huaweicloudsdkbss.v2.DemandProductInfo`]
        """
        
        

        self._project_id = None
        self._inquiry_precision = None
        self._product_infos = None
        self.discriminator = None

        self.project_id = project_id
        if inquiry_precision is not None:
            self.inquiry_precision = inquiry_precision
        self.product_infos = product_infos

    @property
    def project_id(self):
        """Gets the project_id of this RateOnDemandReq.

        项目ID。  说明： 使用客户Token，可以调用[通过assume_role方式获取用户token](https://support.huaweicloud.com/api-iam/iam_30_0003.html)接口获取“regionId”的取值对应的“project id”。具体请参见[如何将合作伙伴Token置换为客户Token](https://support.huaweicloud.com/bpconsole_faq/bpconsole_apifaq_00001.html)的步骤2。IAM子用户调用此接口，需要IAM主账号授权，具体请参考[创建用户组并授权](https://support.huaweicloud.com/usermanual-iam/iam_03_0001.html)。

        :return: The project_id of this RateOnDemandReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RateOnDemandReq.

        项目ID。  说明： 使用客户Token，可以调用[通过assume_role方式获取用户token](https://support.huaweicloud.com/api-iam/iam_30_0003.html)接口获取“regionId”的取值对应的“project id”。具体请参见[如何将合作伙伴Token置换为客户Token](https://support.huaweicloud.com/bpconsole_faq/bpconsole_apifaq_00001.html)的步骤2。IAM子用户调用此接口，需要IAM主账号授权，具体请参考[创建用户组并授权](https://support.huaweicloud.com/usermanual-iam/iam_03_0001.html)。

        :param project_id: The project_id of this RateOnDemandReq.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def inquiry_precision(self):
        """Gets the inquiry_precision of this RateOnDemandReq.

        查询价格结果的精度模式。 0：询价结果默认精度截取，即最长保留到元后6位小数点，如0.000001元1：询价结果保留10位精度，即最长保留到元后10位小数点，如1.0000000001元  说明： 如果询价结果只到元后2位或者3位，那么价格也只到元后2位或者3位，不管传0或者传1都一样，只有询价结果到了小数点后面6位以上，传0和传1才有区别。

        :return: The inquiry_precision of this RateOnDemandReq.
        :rtype: int
        """
        return self._inquiry_precision

    @inquiry_precision.setter
    def inquiry_precision(self, inquiry_precision):
        """Sets the inquiry_precision of this RateOnDemandReq.

        查询价格结果的精度模式。 0：询价结果默认精度截取，即最长保留到元后6位小数点，如0.000001元1：询价结果保留10位精度，即最长保留到元后10位小数点，如1.0000000001元  说明： 如果询价结果只到元后2位或者3位，那么价格也只到元后2位或者3位，不管传0或者传1都一样，只有询价结果到了小数点后面6位以上，传0和传1才有区别。

        :param inquiry_precision: The inquiry_precision of this RateOnDemandReq.
        :type inquiry_precision: int
        """
        self._inquiry_precision = inquiry_precision

    @property
    def product_infos(self):
        """Gets the product_infos of this RateOnDemandReq.

        产品信息列表，询价时要询价产品的信息的列表，具体参见表1。

        :return: The product_infos of this RateOnDemandReq.
        :rtype: list[:class:`huaweicloudsdkbss.v2.DemandProductInfo`]
        """
        return self._product_infos

    @product_infos.setter
    def product_infos(self, product_infos):
        """Sets the product_infos of this RateOnDemandReq.

        产品信息列表，询价时要询价产品的信息的列表，具体参见表1。

        :param product_infos: The product_infos of this RateOnDemandReq.
        :type product_infos: list[:class:`huaweicloudsdkbss.v2.DemandProductInfo`]
        """
        self._product_infos = product_infos

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
        if not isinstance(other, RateOnDemandReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
