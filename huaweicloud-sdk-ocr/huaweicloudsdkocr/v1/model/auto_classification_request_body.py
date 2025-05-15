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
        'pdf_page_number': 'int',
        'extended_parameters': 'object',
        'detect_seal': 'bool'
    }

    attribute_map = {
        'image': 'image',
        'url': 'url',
        'type_list': 'type_list',
        'pdf_page_number': 'pdf_page_number',
        'extended_parameters': 'extended_parameters',
        'detect_seal': 'detect_seal'
    }

    def __init__(self, image=None, url=None, type_list=None, pdf_page_number=None, extended_parameters=None, detect_seal=None):
        r"""AutoClassificationRequestBody

        The model defined in huaweicloud sdk

        :param image: 与url二选一。  图片的Base64编码，要求单个图片、PDF、OFD文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、PDF、OFD格式,OFD格式数据仅支持增值税发票服务。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   
        :type image: str
        :param url: 与image二选一。  单个图片、PDF、OFD文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、PDF、OFD格式,OFD格式数据仅支持增值税发票服务。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 &gt; 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 
        :type url: str
        :param type_list: 可以指定要识别的票证，指定后不出现在此List的票证不识别。不指定时默认返回所有支持类别票证的识别信息。 
        :type type_list: list[str]
        :param pdf_page_number: 指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。  &gt; 说明：  - 如果需要指定PDF页码识别，请通过该参数传入页码。目前不支持通过extended_parameters参数指定票证PDF页码。 
        :type pdf_page_number: int
        :param extended_parameters: 可指定需要识别票证的传入参数，具体参数可参考各票证API文档。若不指定则默认传入image 。 当前版本支持票证类型如下： - vat_invoice：增值税发票  - quota_invoice：定额发票  - taxi_invoice：出租车票  - train_ticket：火车票  - flight_itinerary：飞机行程单  - toll_invoice：车辆通行费发票  - mvs_invoice：机动车销售发票  - id_card：身份证  - passport：护照  - driver_license：驾驶证  - vehicle_license：行驶证  - transportation_license：道路运输证  - bankcard：银行卡  - bus_ship_ticket：车船票  - ride_hailing_itinerary：网约车行程单  - machine_printed_invoice：通用机打发票 &gt; 说明： - 若指定票证参数填写错误会导致该票证识别错误，会提示\&quot;AIS.0101\&quot;:\&quot;The input parameter is invalid.\&quot;报错。 
        :type extended_parameters: object
        :param detect_seal: 检测印章开关，开启时则返回单张票证是否含有印章，否则不返回是否含有印章。可选值包括： - true：开启检测票证是否含有印章功能。  - false：关闭检测票证是否含有印章功能。 &gt; 说明： - 该功能仅检测判断有无印章，不返回印章具体内容。 
        :type detect_seal: bool
        """
        
        

        self._image = None
        self._url = None
        self._type_list = None
        self._pdf_page_number = None
        self._extended_parameters = None
        self._detect_seal = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if url is not None:
            self.url = url
        if type_list is not None:
            self.type_list = type_list
        if pdf_page_number is not None:
            self.pdf_page_number = pdf_page_number
        if extended_parameters is not None:
            self.extended_parameters = extended_parameters
        if detect_seal is not None:
            self.detect_seal = detect_seal

    @property
    def image(self):
        r"""Gets the image of this AutoClassificationRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片、PDF、OFD文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、PDF、OFD格式,OFD格式数据仅支持增值税发票服务。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :return: The image of this AutoClassificationRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this AutoClassificationRequestBody.

        与url二选一。  图片的Base64编码，要求单个图片、PDF、OFD文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、PDF、OFD格式,OFD格式数据仅支持增值税发票服务。  图片文件Base64编码字符串，点击[这里](https://support.huaweicloud.com/ocr_faq/ocr_01_0032.html)查看详细获取方式。   

        :param image: The image of this AutoClassificationRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def url(self):
        r"""Gets the url of this AutoClassificationRequestBody.

        与image二选一。  单个图片、PDF、OFD文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、PDF、OFD格式,OFD格式数据仅支持增值税发票服务。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :return: The url of this AutoClassificationRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AutoClassificationRequestBody.

        与image二选一。  单个图片、PDF、OFD文件其对应的Base64编码不超过10MB。文件在Base64编码后会大于文件原本大小，请注意做好边界判断，建议文件大小不超过7MB。 图片最小边不小于15px，最长边不超过8192px，支持JPEG、JPG、PNG、BMP、TIFF、PDF、OFD格式,OFD格式数据仅支持增值税发票服务。 图片的URL路径，目前支持： - 公网http/https url - OBS提供的url，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权，详情参见[配置OBS访问权限](https://support.huaweicloud.com/api-ocr/ocr_03_0132.html)。 > 说明： - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 - 请保证被检测图片所在的存储服务稳定可靠，推荐使用OBS服务存储图片数据。 - url中不能存在中文字符，若存在，中文需要进行utf8编码。 

        :param url: The url of this AutoClassificationRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def type_list(self):
        r"""Gets the type_list of this AutoClassificationRequestBody.

        可以指定要识别的票证，指定后不出现在此List的票证不识别。不指定时默认返回所有支持类别票证的识别信息。 

        :return: The type_list of this AutoClassificationRequestBody.
        :rtype: list[str]
        """
        return self._type_list

    @type_list.setter
    def type_list(self, type_list):
        r"""Sets the type_list of this AutoClassificationRequestBody.

        可以指定要识别的票证，指定后不出现在此List的票证不识别。不指定时默认返回所有支持类别票证的识别信息。 

        :param type_list: The type_list of this AutoClassificationRequestBody.
        :type type_list: list[str]
        """
        self._type_list = type_list

    @property
    def pdf_page_number(self):
        r"""Gets the pdf_page_number of this AutoClassificationRequestBody.

        指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。  > 说明：  - 如果需要指定PDF页码识别，请通过该参数传入页码。目前不支持通过extended_parameters参数指定票证PDF页码。 

        :return: The pdf_page_number of this AutoClassificationRequestBody.
        :rtype: int
        """
        return self._pdf_page_number

    @pdf_page_number.setter
    def pdf_page_number(self, pdf_page_number):
        r"""Sets the pdf_page_number of this AutoClassificationRequestBody.

        指定PDF页码识别。传入该参数时，则识别指定页码的内容。如果不传该参数，则默认识别第1页。  > 说明：  - 如果需要指定PDF页码识别，请通过该参数传入页码。目前不支持通过extended_parameters参数指定票证PDF页码。 

        :param pdf_page_number: The pdf_page_number of this AutoClassificationRequestBody.
        :type pdf_page_number: int
        """
        self._pdf_page_number = pdf_page_number

    @property
    def extended_parameters(self):
        r"""Gets the extended_parameters of this AutoClassificationRequestBody.

        可指定需要识别票证的传入参数，具体参数可参考各票证API文档。若不指定则默认传入image 。 当前版本支持票证类型如下： - vat_invoice：增值税发票  - quota_invoice：定额发票  - taxi_invoice：出租车票  - train_ticket：火车票  - flight_itinerary：飞机行程单  - toll_invoice：车辆通行费发票  - mvs_invoice：机动车销售发票  - id_card：身份证  - passport：护照  - driver_license：驾驶证  - vehicle_license：行驶证  - transportation_license：道路运输证  - bankcard：银行卡  - bus_ship_ticket：车船票  - ride_hailing_itinerary：网约车行程单  - machine_printed_invoice：通用机打发票 > 说明： - 若指定票证参数填写错误会导致该票证识别错误，会提示\"AIS.0101\":\"The input parameter is invalid.\"报错。 

        :return: The extended_parameters of this AutoClassificationRequestBody.
        :rtype: object
        """
        return self._extended_parameters

    @extended_parameters.setter
    def extended_parameters(self, extended_parameters):
        r"""Sets the extended_parameters of this AutoClassificationRequestBody.

        可指定需要识别票证的传入参数，具体参数可参考各票证API文档。若不指定则默认传入image 。 当前版本支持票证类型如下： - vat_invoice：增值税发票  - quota_invoice：定额发票  - taxi_invoice：出租车票  - train_ticket：火车票  - flight_itinerary：飞机行程单  - toll_invoice：车辆通行费发票  - mvs_invoice：机动车销售发票  - id_card：身份证  - passport：护照  - driver_license：驾驶证  - vehicle_license：行驶证  - transportation_license：道路运输证  - bankcard：银行卡  - bus_ship_ticket：车船票  - ride_hailing_itinerary：网约车行程单  - machine_printed_invoice：通用机打发票 > 说明： - 若指定票证参数填写错误会导致该票证识别错误，会提示\"AIS.0101\":\"The input parameter is invalid.\"报错。 

        :param extended_parameters: The extended_parameters of this AutoClassificationRequestBody.
        :type extended_parameters: object
        """
        self._extended_parameters = extended_parameters

    @property
    def detect_seal(self):
        r"""Gets the detect_seal of this AutoClassificationRequestBody.

        检测印章开关，开启时则返回单张票证是否含有印章，否则不返回是否含有印章。可选值包括： - true：开启检测票证是否含有印章功能。  - false：关闭检测票证是否含有印章功能。 > 说明： - 该功能仅检测判断有无印章，不返回印章具体内容。 

        :return: The detect_seal of this AutoClassificationRequestBody.
        :rtype: bool
        """
        return self._detect_seal

    @detect_seal.setter
    def detect_seal(self, detect_seal):
        r"""Sets the detect_seal of this AutoClassificationRequestBody.

        检测印章开关，开启时则返回单张票证是否含有印章，否则不返回是否含有印章。可选值包括： - true：开启检测票证是否含有印章功能。  - false：关闭检测票证是否含有印章功能。 > 说明： - 该功能仅检测判断有无印章，不返回印章具体内容。 

        :param detect_seal: The detect_seal of this AutoClassificationRequestBody.
        :type detect_seal: bool
        """
        self._detect_seal = detect_seal

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
