# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PubInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logo_img': 'str',
        'pub_name': 'str',
        'pub_abstract': 'str',
        'pub_remark': 'str',
        'auto_get_port': 'int',
        'signs_for_auto_get_port': 'list[str]',
        'industry': 'int',
        'authorization_files': 'list[str]'
    }

    attribute_map = {
        'logo_img': 'logo_img',
        'pub_name': 'pub_name',
        'pub_abstract': 'pub_abstract',
        'pub_remark': 'pub_remark',
        'auto_get_port': 'auto_get_port',
        'signs_for_auto_get_port': 'signs_for_auto_get_port',
        'industry': 'industry',
        'authorization_files': 'authorization_files'
    }

    def __init__(self, logo_img=None, pub_name=None, pub_abstract=None, pub_remark=None, auto_get_port=None, signs_for_auto_get_port=None, industry=None, authorization_files=None):
        """PubInfoRequestBody

        The model defined in huaweicloud sdk

        :param logo_img: 服务号LOGO图片ID。  &gt; 通过上传智能信息服务号图片资源接口上传LOGO图片后获得的图片resource_id。图片要求大于等于240*240且比例相同。 
        :type logo_img: str
        :param pub_name: 服务号名称。  &gt; 同一个企业下可以相同，不同企业下不能重复。 
        :type pub_name: str
        :param pub_abstract: 服务号简介。
        :type pub_abstract: str
        :param pub_remark: 服务号备注。  &gt; 同一个企业下，服务号名称相同时该项必须不同。 
        :type pub_remark: str
        :param auto_get_port: 是否授权系统自动收集端口。   - 0：否 - 1：是 
        :type auto_get_port: int
        :param signs_for_auto_get_port: 自动收集端口使用的签名列表。  &gt; auto_get_port为1时，该字段为必填，每个签名长度为2-18个字符，每个服务号签名不可以重复。 
        :type signs_for_auto_get_port: list[str]
        :param industry: 从事行业，默认取服务号所属商家的行业分类。  - 1：金融理财  - 2：社交通讯  - 3：影音娱乐  - 4：旅游出行  - 5：购物  - 6：本地生活  - 7：运动健康  - 8：教育培训  - 9：新闻阅读  - 10：运营商  - 11：其他 
        :type industry: int
        :param authorization_files: 授权证明图片ID，最多支持6张。  &gt; 参数值为上传智能信息服务号图片资源API返回的resource_id。 
        :type authorization_files: list[str]
        """
        
        

        self._logo_img = None
        self._pub_name = None
        self._pub_abstract = None
        self._pub_remark = None
        self._auto_get_port = None
        self._signs_for_auto_get_port = None
        self._industry = None
        self._authorization_files = None
        self.discriminator = None

        self.logo_img = logo_img
        self.pub_name = pub_name
        self.pub_abstract = pub_abstract
        if pub_remark is not None:
            self.pub_remark = pub_remark
        if auto_get_port is not None:
            self.auto_get_port = auto_get_port
        if signs_for_auto_get_port is not None:
            self.signs_for_auto_get_port = signs_for_auto_get_port
        if industry is not None:
            self.industry = industry
        self.authorization_files = authorization_files

    @property
    def logo_img(self):
        """Gets the logo_img of this PubInfoRequestBody.

        服务号LOGO图片ID。  > 通过上传智能信息服务号图片资源接口上传LOGO图片后获得的图片resource_id。图片要求大于等于240*240且比例相同。 

        :return: The logo_img of this PubInfoRequestBody.
        :rtype: str
        """
        return self._logo_img

    @logo_img.setter
    def logo_img(self, logo_img):
        """Sets the logo_img of this PubInfoRequestBody.

        服务号LOGO图片ID。  > 通过上传智能信息服务号图片资源接口上传LOGO图片后获得的图片resource_id。图片要求大于等于240*240且比例相同。 

        :param logo_img: The logo_img of this PubInfoRequestBody.
        :type logo_img: str
        """
        self._logo_img = logo_img

    @property
    def pub_name(self):
        """Gets the pub_name of this PubInfoRequestBody.

        服务号名称。  > 同一个企业下可以相同，不同企业下不能重复。 

        :return: The pub_name of this PubInfoRequestBody.
        :rtype: str
        """
        return self._pub_name

    @pub_name.setter
    def pub_name(self, pub_name):
        """Sets the pub_name of this PubInfoRequestBody.

        服务号名称。  > 同一个企业下可以相同，不同企业下不能重复。 

        :param pub_name: The pub_name of this PubInfoRequestBody.
        :type pub_name: str
        """
        self._pub_name = pub_name

    @property
    def pub_abstract(self):
        """Gets the pub_abstract of this PubInfoRequestBody.

        服务号简介。

        :return: The pub_abstract of this PubInfoRequestBody.
        :rtype: str
        """
        return self._pub_abstract

    @pub_abstract.setter
    def pub_abstract(self, pub_abstract):
        """Sets the pub_abstract of this PubInfoRequestBody.

        服务号简介。

        :param pub_abstract: The pub_abstract of this PubInfoRequestBody.
        :type pub_abstract: str
        """
        self._pub_abstract = pub_abstract

    @property
    def pub_remark(self):
        """Gets the pub_remark of this PubInfoRequestBody.

        服务号备注。  > 同一个企业下，服务号名称相同时该项必须不同。 

        :return: The pub_remark of this PubInfoRequestBody.
        :rtype: str
        """
        return self._pub_remark

    @pub_remark.setter
    def pub_remark(self, pub_remark):
        """Sets the pub_remark of this PubInfoRequestBody.

        服务号备注。  > 同一个企业下，服务号名称相同时该项必须不同。 

        :param pub_remark: The pub_remark of this PubInfoRequestBody.
        :type pub_remark: str
        """
        self._pub_remark = pub_remark

    @property
    def auto_get_port(self):
        """Gets the auto_get_port of this PubInfoRequestBody.

        是否授权系统自动收集端口。   - 0：否 - 1：是 

        :return: The auto_get_port of this PubInfoRequestBody.
        :rtype: int
        """
        return self._auto_get_port

    @auto_get_port.setter
    def auto_get_port(self, auto_get_port):
        """Sets the auto_get_port of this PubInfoRequestBody.

        是否授权系统自动收集端口。   - 0：否 - 1：是 

        :param auto_get_port: The auto_get_port of this PubInfoRequestBody.
        :type auto_get_port: int
        """
        self._auto_get_port = auto_get_port

    @property
    def signs_for_auto_get_port(self):
        """Gets the signs_for_auto_get_port of this PubInfoRequestBody.

        自动收集端口使用的签名列表。  > auto_get_port为1时，该字段为必填，每个签名长度为2-18个字符，每个服务号签名不可以重复。 

        :return: The signs_for_auto_get_port of this PubInfoRequestBody.
        :rtype: list[str]
        """
        return self._signs_for_auto_get_port

    @signs_for_auto_get_port.setter
    def signs_for_auto_get_port(self, signs_for_auto_get_port):
        """Sets the signs_for_auto_get_port of this PubInfoRequestBody.

        自动收集端口使用的签名列表。  > auto_get_port为1时，该字段为必填，每个签名长度为2-18个字符，每个服务号签名不可以重复。 

        :param signs_for_auto_get_port: The signs_for_auto_get_port of this PubInfoRequestBody.
        :type signs_for_auto_get_port: list[str]
        """
        self._signs_for_auto_get_port = signs_for_auto_get_port

    @property
    def industry(self):
        """Gets the industry of this PubInfoRequestBody.

        从事行业，默认取服务号所属商家的行业分类。  - 1：金融理财  - 2：社交通讯  - 3：影音娱乐  - 4：旅游出行  - 5：购物  - 6：本地生活  - 7：运动健康  - 8：教育培训  - 9：新闻阅读  - 10：运营商  - 11：其他 

        :return: The industry of this PubInfoRequestBody.
        :rtype: int
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this PubInfoRequestBody.

        从事行业，默认取服务号所属商家的行业分类。  - 1：金融理财  - 2：社交通讯  - 3：影音娱乐  - 4：旅游出行  - 5：购物  - 6：本地生活  - 7：运动健康  - 8：教育培训  - 9：新闻阅读  - 10：运营商  - 11：其他 

        :param industry: The industry of this PubInfoRequestBody.
        :type industry: int
        """
        self._industry = industry

    @property
    def authorization_files(self):
        """Gets the authorization_files of this PubInfoRequestBody.

        授权证明图片ID，最多支持6张。  > 参数值为上传智能信息服务号图片资源API返回的resource_id。 

        :return: The authorization_files of this PubInfoRequestBody.
        :rtype: list[str]
        """
        return self._authorization_files

    @authorization_files.setter
    def authorization_files(self, authorization_files):
        """Sets the authorization_files of this PubInfoRequestBody.

        授权证明图片ID，最多支持6张。  > 参数值为上传智能信息服务号图片资源API返回的resource_id。 

        :param authorization_files: The authorization_files of this PubInfoRequestBody.
        :type authorization_files: list[str]
        """
        self._authorization_files = authorization_files

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
        if not isinstance(other, PubInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
