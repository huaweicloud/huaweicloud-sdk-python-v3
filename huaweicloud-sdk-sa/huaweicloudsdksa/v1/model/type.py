# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Type:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'business': 'str',
        'category': 'str',
        'classifier': 'str',
        'tech_domain': 'str',
        'properties': 'TypeProperties'
    }

    attribute_map = {
        'business': 'business',
        'category': 'category',
        'classifier': 'classifier',
        'tech_domain': 'tech_domain',
        'properties': 'properties'
    }

    def __init__(self, business=None, category=None, classifier=None, tech_domain=None, properties=None):
        """Type

        The model defined in huaweicloud sdk

        :param business: 事件所属业务领域标签，可选类别如下： attack – 攻击 vulnerability – 漏洞 compliance check – 合规检查 risk - 风险 public opinion - 舆情 illegal&amp;violation - 违法违规 security bulletin - 公告
        :type business: str
        :param category: 类别，推荐使用预定义的类型分类。
        :type category: str
        :param classifier: 分类器，推荐使用预定义的分类器。 如果指定了分类器，则必须指定类别。
        :type classifier: str
        :param tech_domain: 技术领域标签： OS：主机 APP：应用 NET：网络 OPS：运维 CS：云服务 CSP：平台云服务
        :type tech_domain: str
        :param properties: 
        :type properties: :class:`huaweicloudsdksa.v1.TypeProperties`
        """
        
        

        self._business = None
        self._category = None
        self._classifier = None
        self._tech_domain = None
        self._properties = None
        self.discriminator = None

        self.business = business
        if category is not None:
            self.category = category
        if classifier is not None:
            self.classifier = classifier
        if tech_domain is not None:
            self.tech_domain = tech_domain
        if properties is not None:
            self.properties = properties

    @property
    def business(self):
        """Gets the business of this Type.

        事件所属业务领域标签，可选类别如下： attack – 攻击 vulnerability – 漏洞 compliance check – 合规检查 risk - 风险 public opinion - 舆情 illegal&violation - 违法违规 security bulletin - 公告

        :return: The business of this Type.
        :rtype: str
        """
        return self._business

    @business.setter
    def business(self, business):
        """Sets the business of this Type.

        事件所属业务领域标签，可选类别如下： attack – 攻击 vulnerability – 漏洞 compliance check – 合规检查 risk - 风险 public opinion - 舆情 illegal&violation - 违法违规 security bulletin - 公告

        :param business: The business of this Type.
        :type business: str
        """
        self._business = business

    @property
    def category(self):
        """Gets the category of this Type.

        类别，推荐使用预定义的类型分类。

        :return: The category of this Type.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Type.

        类别，推荐使用预定义的类型分类。

        :param category: The category of this Type.
        :type category: str
        """
        self._category = category

    @property
    def classifier(self):
        """Gets the classifier of this Type.

        分类器，推荐使用预定义的分类器。 如果指定了分类器，则必须指定类别。

        :return: The classifier of this Type.
        :rtype: str
        """
        return self._classifier

    @classifier.setter
    def classifier(self, classifier):
        """Sets the classifier of this Type.

        分类器，推荐使用预定义的分类器。 如果指定了分类器，则必须指定类别。

        :param classifier: The classifier of this Type.
        :type classifier: str
        """
        self._classifier = classifier

    @property
    def tech_domain(self):
        """Gets the tech_domain of this Type.

        技术领域标签： OS：主机 APP：应用 NET：网络 OPS：运维 CS：云服务 CSP：平台云服务

        :return: The tech_domain of this Type.
        :rtype: str
        """
        return self._tech_domain

    @tech_domain.setter
    def tech_domain(self, tech_domain):
        """Sets the tech_domain of this Type.

        技术领域标签： OS：主机 APP：应用 NET：网络 OPS：运维 CS：云服务 CSP：平台云服务

        :param tech_domain: The tech_domain of this Type.
        :type tech_domain: str
        """
        self._tech_domain = tech_domain

    @property
    def properties(self):
        """Gets the properties of this Type.


        :return: The properties of this Type.
        :rtype: :class:`huaweicloudsdksa.v1.TypeProperties`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Type.


        :param properties: The properties of this Type.
        :type properties: :class:`huaweicloudsdksa.v1.TypeProperties`
        """
        self._properties = properties

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
        if not isinstance(other, Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
