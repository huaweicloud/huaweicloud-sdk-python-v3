# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoClassificationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image': 'str',
        'url': 'str',
        'type_list': 'list[str]',
        'extended_parameters': 'object'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'type_list': 'type_list',
        'extended_parameters': 'extended_parameters'
    }

    def __init__(self, image=None, url=None, type_list=None, extended_parameters=None):
        """AutoClassificationRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过8000px，支持JPEG、JPG、PNG、BMP、TIFF、PDF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param type_list: 可以指定要识别的票证，指定后不出现在此List的票证不识别。不指定时默认返回所有支持类别票证的识别信息。 
        :type type_list: list[str]
        :param extended_parameters: 可指定需要识别票证的传入参数，具体参数可参考各票证API文档。若不指定则默认传入image 。 当前版本支持票证类型如下： - vat_invoice：增值税发票  - quota_invoice：定额发票  - taxi_invoice：出租车票  - train_ticket：火车票  - flight_itinerary：飞机行程单  - toll_invoice：车辆通行费发票  - mvs_invoice：机动车销售发票  - id_card：身份证  - passport：护照  - driver_license：驾驶证  - vehicle_license：行驶证  - transportation_license：道路运输证  - bankcard：银行卡 &gt; 说明： - 若指定票证参数填写错误会导致该票证识别错误，会提示\&quot;AIS.0101\&quot;:\&quot;The input parameter is invalid.\&quot;报错。 
        :type extended_parameters: object
        """
        
        

        self._image = None
        self._url = None
        self._type_list = None
        self._extended_parameters = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if type_list is not None:
            self.type_list = type_list
        if extended_parameters is not None:
            self.extended_parameters = extended_parameters

    @property
    def image(self):
        """Gets the image of this AutoClassificationRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过8000px，支持JPEG、JPG、PNG、BMP、TIFF、PDF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this AutoClassificationRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this AutoClassificationRequestBody.

        与url二选一  图像数据，base64编码，要求base64编码后大小不超过10MB。图片最小边不小于15px，最长边不超过8000px，支持JPEG、JPG、PNG、BMP、TIFF、PDF格式。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this AutoClassificationRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        """Gets the url of this AutoClassificationRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this AutoClassificationRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AutoClassificationRequestBody.

        与image二选一 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this AutoClassificationRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def type_list(self):
        """Gets the type_list of this AutoClassificationRequestBody.

        可以指定要识别的票证，指定后不出现在此List的票证不识别。不指定时默认返回所有支持类别票证的识别信息。 

        :return: The type_list of this AutoClassificationRequestBody.
        :rtype: list[str]
        """
        return self._type_list

    @type_list.setter
    def type_list(self, type_list):
        """Sets the type_list of this AutoClassificationRequestBody.

        可以指定要识别的票证，指定后不出现在此List的票证不识别。不指定时默认返回所有支持类别票证的识别信息。 

        :param type_list: The type_list of this AutoClassificationRequestBody.
        :type type_list: list[str]
        """
        self._type_list = type_list

    @property
    def extended_parameters(self):
        """Gets the extended_parameters of this AutoClassificationRequestBody.

        可指定需要识别票证的传入参数，具体参数可参考各票证API文档。若不指定则默认传入image 。 当前版本支持票证类型如下： - vat_invoice：增值税发票  - quota_invoice：定额发票  - taxi_invoice：出租车票  - train_ticket：火车票  - flight_itinerary：飞机行程单  - toll_invoice：车辆通行费发票  - mvs_invoice：机动车销售发票  - id_card：身份证  - passport：护照  - driver_license：驾驶证  - vehicle_license：行驶证  - transportation_license：道路运输证  - bankcard：银行卡 > 说明： - 若指定票证参数填写错误会导致该票证识别错误，会提示\"AIS.0101\":\"The input parameter is invalid.\"报错。 

        :return: The extended_parameters of this AutoClassificationRequestBody.
        :rtype: object
        """
        return self._extended_parameters

    @extended_parameters.setter
    def extended_parameters(self, extended_parameters):
        """Sets the extended_parameters of this AutoClassificationRequestBody.

        可指定需要识别票证的传入参数，具体参数可参考各票证API文档。若不指定则默认传入image 。 当前版本支持票证类型如下： - vat_invoice：增值税发票  - quota_invoice：定额发票  - taxi_invoice：出租车票  - train_ticket：火车票  - flight_itinerary：飞机行程单  - toll_invoice：车辆通行费发票  - mvs_invoice：机动车销售发票  - id_card：身份证  - passport：护照  - driver_license：驾驶证  - vehicle_license：行驶证  - transportation_license：道路运输证  - bankcard：银行卡 > 说明： - 若指定票证参数填写错误会导致该票证识别错误，会提示\"AIS.0101\":\"The input parameter is invalid.\"报错。 

        :param extended_parameters: The extended_parameters of this AutoClassificationRequestBody.
        :type extended_parameters: object
        """
        self._extended_parameters = extended_parameters

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
        if not isinstance(other, AutoClassificationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
